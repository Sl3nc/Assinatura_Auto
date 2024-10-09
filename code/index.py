from src.window_ass import Ui_MainWindow
from PySide6.QtWidgets import (QMainWindow, QApplication, QWidget)
from docxtpl import DocxTemplate, InlineImage
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
from spire.doc import Document, ImageType
from docx.shared import Mm
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

class Texto:
    def __init__(self) -> None:
        self.complemento = Arquivo(resource_path('src\\base_texto.docx'))
        self.KEY_IMG = 'img'
        pass

    def add_img(self, img, nome_arq: str):
        myimage = InlineImage(
            self.complemento, img, width=Mm(20), height=Mm(10))

        ref = {self.KEY_IMG: myimage}

        self.complemento.renderizar(ref, nome_arq)

class Assinatura:
    def __init__(self) -> None:
        self.modelo = Arquivo(resource_path('src\\base_assinaturas.docx'))
        self.endereco_email = '@deltaprice.com.br'

        self.nome_arq = 'assin_word.docx'
        self.nome_png = 'page.png'

        self.KEY_NOME = 'nome'
        self.KEY_SETOR = 'setor'
        pass

    def preencher_modelo(self, nome_func: str, setor: str):
        ref = {
            self.KEY_NOME: nome_func,
            self.KEY_SETOR: setor + self.endereco_email
        }

        self.modelo.renderizar(ref, self.nome_arq)

    def gerar_png(self):
        # Create a Document object
        document = Document(self.nome_arq)
        # Convert a specific page to bitmap image
        imageStream = document.SaveImageToStreams(0, ImageType.Bitmap)
    
        # Save the bitmap to a PNG file
        with open(self.nome_png,'wb') as imageFile:
            imageFile.write(imageStream.ToArray())
        document.Close()

        os.remove(self.nome_arq)

        return self.nome_arq

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(
            self.executar)

        self.lineEdit.setPlaceholderText('Preencha aqui')

        self.comboBox.setPlaceholderText('Selecione a opção')
        self.comboBox.addItems(
            ['Processos', 'Financeiro', 'Fiscal', 'Contabilidade', 'Trabalhista']
            )

    def executar(self):
        # try:
            if self.lineEdit.text() == '':
                raise Exception('Favor insirir seu nome!')
            elif self.comboBox.currentText() == '':
                raise Exception('Favor selecione seu setor!')
            
            ass = Assinatura()
            txt = Texto()

            ass.preencher_modelo(
                self.lineEdit.text(), self.comboBox.currentText().lower())

            nome_img = ass.gerar_png()
            nome_arq = self.onde_salvar()

            txt.add_img(nome_img, nome_arq)

            # messagebox.showinfo(title='Aviso', message='Abrindo o arquivo gerado!')

            # os.startfile(nome_arq+'.docx')
            
        # except Exception as error:
        #     messagebox.showerror(title='Aviso', message= str(error))

    def onde_salvar(self):
        file = asksaveasfilename(title='Favor selecionar a pasta onde será salvo', filetypes=((".docx","*.docx"),))

        if file == '':
            resp = messagebox.askyesno(title='Deseja cancelar a operação?', filetypes=((".docx","*.docx"),))
            if resp == True:
                raise 'Operação cancelada!'
            else:
                return self.onde_salvar()

        return file

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()