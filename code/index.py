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
from pathlib import Path

class Arquivo:
    def __init__(self, caminho: str) -> None:
        self.caminho = DocxTemplate(caminho)
        pass

    def renderizar(self, ref: dict, path: str):
        self.caminho.render(ref)
        self.caminho.save(path)

    def enquadro(self, img:str):
        return InlineImage(self.caminho, img, width=Mm(100))

class Imagem:
    def __init__(self) -> None:
        self.AREA_CORTE = (0, 50, 1524, 564)
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
        self.base_ass = Arquivo(
            (Path(__file__).parent/'src'/'bases'/'base_assinaturas_25y.docx').__str__()
        )
        self.base_texto = Arquivo(
            (Path(__file__).parent/'src'/'bases'/'base_texto.docx').__str__()
        )

        self.ENDR_EMAIL = '@deltaprice.com.br'

        self.NOME_ARQ = 'assin_word.docx'
        self.NOME_PNG = 'page.png'

        self.KEY_NOME = 'nome'
        self.KEY_SETOR = 'setor'
        self.KEY_IMG = 'img'
        pass

    def preencher_modelo(self, nome_func: str, setor: str):
        ref = {
            self.KEY_NOME: nome_func,
            self.KEY_SETOR: setor + self.ENDR_EMAIL
        }

        self.base_ass.renderizar(ref, self.NOME_ARQ)

    def add_img(self, nome_arq: str):
        # Create a Document object
        Imagem().gerar_png(self.NOME_PNG, self.NOME_ARQ)
        os.remove(self.NOME_ARQ)

        my_image = self.base_texto.enquadro(self.NOME_PNG)
        
        ref = {self.KEY_IMG: my_image}
        self.base_texto.renderizar(ref, nome_arq+'.docx')
        os.remove(self.NOME_PNG)

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
            ass.add_img(self.nome_arq)
            self.fim.emit(False)
        except Exception as err:
            print(traceback.print_exc())
            messagebox.showerror('Aviso', err)

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowIcon((QIcon(
            (Path(__file__).parent/'src'/'imgs'/'ass-icon.ico').__str__()
        )))
        self.logo_hori.setPixmap(QPixmap(
            (Path(__file__).parent/'src'/'imgs'/'ass-hori.png').__str__()
        ))
        self.movie = QMovie(
            (Path(__file__).parent/'src'/'imgs'/'load.gif').__str__()
        )
        self.gif_load.setMovie(self.movie)

        self.pushButton.clicked.connect(
            self.executar)

        self.setor_exption = 'Não exibir*'

        self.comboBox.setPlaceholderText('Selecione a opção')
        self.comboBox.addItems(
            ['Processos', 'Financeiro', 'Fiscal', 'Contabilidade', 'Trabalhista', self.setor_exption]
            )

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
            setor = '' if setor == self.setor_exption else setor.lower()

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
            os.startfile(self.nome_arq+'.docx')

    def onde_salvar(self):
        return asksaveasfilename(title='Favor selecionar a pasta onde será salvo', filetypes=((".docx","*.docx"),))

        # if file == '':
        #     return self.retry_save()

    def retry_save(self):
        resp = messagebox.askyesno(title='Deseja cancelar a operação?', filetypes=((".docx","*.docx"),))
        if resp == True:
            raise 'Operação cancelada!'
        else:
            return self.onde_salvar()

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()