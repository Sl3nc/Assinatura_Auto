from PySide6.QtCore import Signal, QObject
from tkinter import messagebox
from assign import Assinatura
from traceback import print_exc

class Worker(QObject):
    """
    Worker para execução em thread separada, evitando travamento da interface.
    """
    inicio = Signal(bool)
    fim = Signal(bool)

    def __init__(self, nome_func: str, setor: str, nome_arq: str) -> None:
        super().__init__()
        self.nome_func = nome_func
        self.setor = setor
        self.nome_arq = nome_arq

    def main(self):
        """
        Executa o processo de geração da assinatura.
        """
        try:
            self.inicio.emit(True)
            ass = Assinatura()
            ass.preencher_modelo(self.nome_func, self.setor)
            ass.add_img(self.nome_arq)
            self.fim.emit(False)
        except Exception as err:
            print(print_exc())
            messagebox.showerror('Aviso', err)
