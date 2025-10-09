from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='Pro-video-ferramentas',
    version=1.0,
    description='Este produto irá fornecer ferramentas de vídeo',
    long_description=Path('README.md').read_text(),
    author='',
    author_email='',
    keywords=['Camera','Video','processamento'],
    packages=find_packages()
)

# Para publicar temos que entrar no site do pip e fazer o nosso registro
# Clica em AccountSettings
# Instale no terminal do vscode a seguinte ferramenta
# pip install setuptools twine
# Dentro da pasta que queremos publicar rodamos o seguinte comando no terminal
# python .\setup.py sdist
# Vai gerar duas pastas 
# Temos que enviar o arquivo dentro da pasta dist
# E rodar o seguinte comando 
# twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
# Vai pedir seu user e senha do site