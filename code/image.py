import spire.doc as sd
from PIL import Image

class Imagem:
    """
    Classe responsável por gerar e cortar imagens a partir de documentos Word.
    """
    def __init__(self) -> None:
        # Área de corte da imagem (esquerda, topo, direita, baixo)
        self.AREA_CORTE = (0, 50, 1524, 564)
        pass

    def gerar_png(self, nome_png : str, nome_arq : str):
        """
        Gera uma imagem PNG da primeira página de um documento Word e realiza o corte.
        """
        document = sd.Document(nome_arq)
        imageStream = document.SaveImageToStreams(0, sd.ImageType.Bitmap)
        with open(nome_png,'wb') as imageFile:
            imageFile.write(imageStream.ToArray())
        document.Close()
        self.__cortar_img(nome_png)

    def __cortar_img(self, nome_png):
        """
        Realiza o corte da imagem gerada, conforme a área definida.
        """
        imagem = Image.open(nome_png)
        imagem_cortada = imagem.crop(self.AREA_CORTE)
        imagem_cortada.save(nome_png)
