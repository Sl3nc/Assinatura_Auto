from pathlib import Path
from file import Arquivo
from os import remove
from image import Imagem

class Assinatura:
    """
    Classe principal para geração de assinaturas automáticas.
    """
    def __init__(self) -> None:
        """
        Inicializa os templates base e define constantes.
        """
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
        """
        Preenche o template de assinatura com nome e setor do funcionário.
        """
        ref = {
            self.KEY_NOME: nome_func,
            self.KEY_SETOR: setor + self.ENDR_EMAIL
        }

        self.base_ass.renderizar(ref, self.NOME_ARQ)

    def add_img(self, nome_arq: str):
        """
        Gera a imagem da assinatura e insere no template final.
        """
        Imagem().gerar_png(self.NOME_PNG, self.NOME_ARQ)
        remove(self.NOME_ARQ)

        my_image = self.base_texto.enquadro(self.NOME_PNG)
        
        ref = {self.KEY_IMG: my_image}
        self.base_texto.renderizar(ref, nome_arq+'.docx')
        remove(self.NOME_PNG)

