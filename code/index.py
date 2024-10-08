from PySide6.QtCore import Qt
from src.window_ass import Ui_MainWindow
from PySide6.QtWidgets import (QMainWindow, QApplication, QWidget)
from docxtpl import DocxTemplate
import sys

def resource_path():
    ...

class Arquivo:
    def __init__(self, caminho) -> None:
        self.caminho = DocxTemplate(caminho)
        pass

    def renderizar(self, nome):
        self.caminho.render()
        self.caminho.save(nome)

class Texto:
    def __init__(self) -> None:
        self.complemento = Arquivo(resource_path('src/'))
        self.KEY_IMG = ''
        pass

    def add(self, img):
        myimage = InlineImage(
            tpl, image_descriptor= img, width=Mm(20), height=Mm(10))

        ref = {self.KEY_IMG: myimage}

        self.complemento.renderizar(ref)

class Assinatura:
    def __init__(self) -> None:
        self.modelo = Arquivo(resource_path('src/'))
        self.KEY_NOME = ''
        self.KEY_SETOR = ''
        pass

    def gerar_png(self, nome, setor):
        ref = {
            self.KEY_NOME: nome,
            self.KEY_SETOR: setor
        }

        ass_word = self.modelo.renderizar(ref)

        doc = aw.Document("ass_word")

        # set output image format
        options = aw.saving.ImageSaveOptions(aw.SaveFormat.PNG)

        options.page_set = aw.saving.PageSet(1)
        doc.save("page.png", options)

        return 'page.png'

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        action_main = self.pushButton.addAction('Gerar Ass.')
        action_main.clicked.connect()

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()