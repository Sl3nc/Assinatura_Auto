# Assinatura Automática

Este projeto é uma aplicação desktop para geração automática de assinaturas personalizadas em documentos Word (.docx), com inserção de informações do usuário e imagem da assinatura. O sistema utiliza interface gráfica baseada em PySide6 (Qt), manipulação de arquivos Word com `docxtpl` e `spire.doc`, além de processamento de imagens com PIL.

## Funcionalidades

- Interface gráfica amigável para entrada de dados do usuário (nome e setor).
- Geração automática de documento de assinatura personalizado.
- Inserção de imagem da assinatura no documento final.
- Processamento em thread separada para não travar a interface.
- Suporte a múltiplos setores e opção para não exibir setor.
- Abertura automática do arquivo gerado ao final do processo.

## Como funciona

1. O usuário informa seu nome e seleciona o setor.
2. O sistema preenche um template Word com essas informações.
3. Uma imagem da assinatura é gerada e inserida em outro template.
4. O documento final é salvo no local escolhido pelo usuário e aberto automaticamente.

## Requisitos

- Python 3.8+
- [PySide6](https://pypi.org/project/PySide6/)
- [docxtpl](https://pypi.org/project/docxtpl/)
- [python-docx](https://pypi.org/project/python-docx/)
- [Pillow (PIL)](https://pypi.org/project/Pillow/)
- [spire.doc](https://www.e-iceblue.com/Introduce/free-doc-component.html) (biblioteca comercial/free para manipulação de Word)
- [tkinter](https://docs.python.org/3/library/tkinter.html) (incluso no Python)

## Instalação

Instale as dependências com pip:

```bash
pip install PySide6 docxtpl python-docx Pillow
```

A biblioteca `spire.doc` deve ser instalada separadamente conforme instruções do fornecedor.

## Uso

1. Execute o arquivo principal:

   ```bash
   python code/index.py
   ```

2. Preencha seu nome e selecione o setor.
3. Escolha onde salvar o arquivo gerado.
4. Aguarde o processamento e o documento será aberto automaticamente.

## Estrutura do Projeto

- `code/index.py`: Código principal da aplicação.
- `src/window_ass.py`: Arquivo gerado pelo Qt Designer (UI).
- `src/bases/`: Templates base `.docx` utilizados.
- `src/imgs/`: Imagens e ícones da interface.

## Observações

- O programa utiliza arquivos de template `.docx` que devem estar presentes na pasta `src/bases/`.
- O ícone e imagens da interface devem estar em `src/imgs/`.
- O processamento de imagens depende do correto funcionamento do `spire.doc`.

## Licença

Este projeto é de uso interno e não possui licença aberta.