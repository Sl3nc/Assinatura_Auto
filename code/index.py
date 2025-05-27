from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QMovie, QIcon, QPixmap
from tkinter.filedialog import asksaveasfilename
from src.window_ass import Ui_MainWindow
from PySide6.QtCore import QThread
from traceback import print_exc
from tkinter import messagebox
from worker import Worker
from pathlib import Path
from os import startfile


class MainWindow(Ui_MainWindow, QMainWindow):
    """
    Classe da janela principal da aplicação.
    """
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
        """
        Inicia o processo de geração da assinatura ao clicar no botão.
        """
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
            print(print_exc())
            messagebox.showerror('Aviso', err)

    def load(self, value: bool):
        """
        Atualiza a interface durante o processamento.
        """
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
            startfile(self.nome_arq+'.docx')

    def onde_salvar(self):
        """
        Abre o diálogo para o usuário escolher onde salvar o arquivo gerado.
        """
        return asksaveasfilename(title='Favor selecionar a pasta onde será salvo', filetypes=((".docx","*.docx"),))

    def retry_save(self):
        """
        Pergunta ao usuário se deseja cancelar ou tentar salvar novamente.
        """
        resp = messagebox.askyesno(title='Deseja cancelar a operação?', filetypes=((".docx","*.docx"),))
        if resp == True:
            raise 'Operação cancelada!'
        else:
            return self.onde_salvar()

if __name__ == '__main__':
    # Inicializa a aplicação Qt
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()