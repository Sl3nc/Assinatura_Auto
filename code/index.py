from PySide6.QtCore import Qt
from src.window_ass import Ui_MainWindow
from PySide6.QtWidgets import (QMainWindow, QApplication, QWidget)
from docxtpl import DocxTemplate, InlineImage
from tkinter import messagebox
from docx.shared import Mm
import aspose.words as aw
import os
import sys

def resource_path(relative_path):
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class Arquivo:
    def __init__(self, caminho) -> None:
        self.caminho = DocxTemplate(caminho)
        pass

    def renderizar(self, nome):
        self.caminho.render()
        self.caminho.save(nome)

class Texto:
    def __init__(self) -> None:
        self.complemento = Arquivo(resource_path('src\\base_texto.docx'))
        self.KEY_IMG = 'img'
        pass

    def add(self, img, nome_arq):
        myimage = InlineImage(
            self.complemento, img, width=Mm(20), height=Mm(10))

        ref = {self.KEY_IMG: myimage}

        self.complemento.renderizar(ref, nome_arq)

class Assinatura:
    def __init__(self) -> None:
        self.nome_arq = 'assin_word.docx'
        self.nome_png = 'page.png'
        self.modelo = Arquivo(resource_path('src\\base_assinaturas.docx'))
        self.KEY_NOME = 'nome'
        self.KEY_SETOR = 'setor'
        pass

    def preencher_modelo(self, nome, setor):
        ref = {
            self.KEY_NOME: nome,
            self.KEY_SETOR: setor
        }

        self.modelo.renderizar(ref, self.nome_arq)

    def gerar_png(self):
        doc = aw.Document(self.nome_arq)

        # set output image format
        options = aw.saving.ImageSaveOptions(aw.SaveFormat.PNG)

        options.page_set = aw.saving.PageSet(1)
        doc.save(self.nome_png, options)

        return self.nome_arq

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        action_main = self.pushButton.addAction('Gerar Ass.')
        action_main.clicked.connect(self.executar())

    def onde_salvar(self):
        file = messagebox.messasksaveasfilename(title='Favor selecionar a pasta onde será salvo', filetypes=((".docx","*.docx"),))

        if file == '':
            resp = messagebox.askyesno(title='Deseja cancelar a operação?', filetypes=((".docx","*.docx"),))
            if resp == True:
                raise 'Operação cancelada!'
            else:
                return self.onde_salvar()

        return file

    def executar(self):
        try:
            if self.comboBox == '':
                raise 'Favor selecione seu setor!'
            elif self.lineEdit == '':
                raise 'Favor insirir seu nome!'
            
            ass = Assinatura()
            txt = Texto()

            ass.preencher_modelo(self.lineEdit, self.comboBox)

            nome_img = ass.gerar_png()
            nome_arq = self.onde_salvar()

            txt.add(nome_img, nome_arq)

            messagebox.showinfo(title='Aviso', message='Abrindo o arquivo gerado!')

            os.startfile(nome_arq+'.docx')
        except:
            Exception

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()