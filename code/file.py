from docxtpl import DocxTemplate
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm

class Arquivo:
    """
    Classe responsável por manipular arquivos de template .docx usando docxtpl.
    """
    def __init__(self, caminho: str) -> None:
        """
        Inicializa o objeto com o caminho do template .docx.
        """
        self.caminho = DocxTemplate(caminho)
        pass

    def renderizar(self, ref: dict, path: str):
        """
        Renderiza o template com os dados fornecidos e salva no caminho especificado.
        """
        self.caminho.render(ref)
        self.caminho.save(path)

    def enquadro(self, img:str):
        """
        Insere uma imagem no template, ajustando seu tamanho.
        """
        return InlineImage(self.caminho, img, width=Mm(100))