from src.window_ass import Ui_MainWindow
from PySide6.QtWidgets import (
    QMainWindow, QApplication, QLabel, QWidget, QGridLayout)
from PySide6.QtGui import QMovie, QIcon, QPixmap
from PySide6.QtCore import QThread, Signal, QObject
from docxtpl import DocxTemplate, InlineImage
from tkinter.filedialog import asksaveasfilename
from PIL import Image
from tkinter import messagebox
import spire.doc as sd
from docx.shared import Mm
import traceback
import time
import os
import sys

def resource_path(relative_path):
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class Arquivo:
    def __init__(self, caminho: str) -> None:
        self.caminho = DocxTemplate(caminho)
        pass

    def renderizar(self, ref: dict, path: str):
        self.caminho.render(ref)
        self.caminho.save(path)

class Imagem:
    def __init__(self) -> None:
        self.AREA_CORTE = (0, 40, 1524, 540)
        #(esquerda, topo, direita, baixo)
        pass

    def gerar_png(self, nome_png : str, nome_arq : str):
        document = sd.Document(nome_arq)
        # Convert a specific page to bitmap image
        imageStream = document.SaveImageToStreams(0, sd.ImageType.Bitmap)
        # Save the bitmap to a PNG file
        with open(nome_png,'wb') as imageFile:
            imageFile.write(imageStream.ToArray())
        document.Close()
        self.__cortar_img(nome_png)

    def __cortar_img(self, nome_png):
        # Abrindo uma imagem
        imagem = Image.open(nome_png)

        # Cortando a imagem 
        imagem_cortada = imagem.crop(self.AREA_CORTE)

        # Salvando a imagem em outro formato
        imagem_cortada.save(nome_png)

class Assinatura:
    def __init__(self) -> None:
        self.base_ass = Arquivo(resource_path('src\\bases\\base_assinaturas_25y.docx'))

        self.NOME_ARQ = 'assin_word.docx'

        self.KEY_NOME = 'nome'
        self.KEY_SETOR = 'setor'
        pass

    def preencher_modelo(self, nome_func: str, setor: str):
        ref = {
            self.KEY_NOME: nome_func,
            self.KEY_SETOR: setor
        }

        self.base_ass.renderizar(ref, self.NOME_ARQ)

    def create_img(self, nome_png: str):
        Imagem().gerar_png(nome_png, self.NOME_ARQ)
        os.remove(self.NOME_ARQ)

class Worker(QObject):
    inicio = Signal(bool)
    fim = Signal(bool)

    def __init__(self, nome_func: str, setor: str, nome_arq: str) -> None:
        super().__init__()
        self.nome_func = nome_func
        self.setor = setor
        self.nome_arq = nome_arq

    def main(self):
        try:
            self.inicio.emit(True)
            ass = Assinatura()
            ass.preencher_modelo(self.nome_func, self.setor)
            ass.create_img(self.nome_arq)
            self.fim.emit(False)
        except Exception as err:
            print(traceback.print_exc())
            messagebox.showerror('Aviso', err)

class MainWindow(Ui_MainWindow, QMainWindow):

    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowIcon((QIcon(resource_path('src\\imgs\\ass-icon.ico'))))
        self.logo_hori.setPixmap(QPixmap(resource_path('src\\imgs\\ass-hori.png')))
        self.movie = QMovie(resource_path("src\\imgs\\load.gif"))
        self.gif_load.setMovie(self.movie)

        self.pushButton.clicked.connect(
            self.executar)

        self.lineEdit.setPlaceholderText('Preencha aqui')
        self.setor_exption = 'Não exibir*'

        self.comboBox.setPlaceholderText('Selecione a opção')
        self.comboBox.addItems(
            ['Processos', 'Financeiro', 'Fiscal', 'Contabilidade', 'Trabalhista', self.setor_exption]
            )

        self.ENDR_EMAIL = '@deltaprice.com.br'

        self.text_load.show()
        self.movie.start()

    def executar(self):
        try:
            if self.lineEdit.text() == '':
                raise Exception('Favor insirir seu nome!')
            elif self.comboBox.currentText() == '':
                raise Exception('Favor selecione seu setor!')

            self.nome_arq =  self.onde_salvar()
            setor = self.comboBox.currentText()
            setor = '' if setor == self.setor_exption else f'\n{setor.lower() + self.ENDR_EMAIL}'

            self._worker = Worker(
                self.lineEdit.text(),
                setor,
                self.nome_arq
                )
            
            self._thread = QThread()
            worker = self._worker
            thread = self._thread

            worker.moveToThread(thread)
            thread.started.connect(worker.main)
            worker.fim.connect(thread.quit)
            worker.fim.connect(thread.deleteLater)
            thread.finished.connect(worker.deleteLater)
            worker.inicio.connect(self.load) 
            worker.fim.connect(self.load) 
            thread.start() 
        except Exception as err:
            print(traceback.print_exc())
            messagebox.showerror('Aviso', err)

    def load(self, value: bool):
        if value == True:
            self.pushButton.setDisabled(True)
            self.stackedWidget.setCurrentIndex(1)
            self.text_load.show()
            self.movie.start()
        elif value == False:
            self.pushButton.setDisabled(False)
            self.stackedWidget.setCurrentIndex(0)
            self.movie.stop()
            self.text_load.hide()
            self.gif_load.hide()
            self.centralwidget.show()
            messagebox.showinfo(title='Aviso', message='Abrindo o arquivo gerado!')
            os.startfile(self.nome_arq)

    def onde_salvar(self):
        file = f'{asksaveasfilename(title='Favor selecionar a pasta onde será salvo', filetypes=((".png","*.png"),))}.png'

        return file if file != '' else self.retry_save()

    def retry_save(self):
        resp = messagebox.askyesno(title='Deseja cancelar a operação?', filetypes=((".png","*.png"),))
        if resp == True:
            raise 'Operação cancelada!'
        else:
            return self.onde_salvar()

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()