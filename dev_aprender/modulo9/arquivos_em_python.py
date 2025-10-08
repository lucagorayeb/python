import os
import shutil as shu

# Listar os
print(os.name) 

# Listar arquivos no diretório atual
print(os.listdir()) 

# Retorna o path do diretório atual
print(os.sep) 

# Retorna o separador nativo do os atual
print(os.getcwd()) 

# Retorna o path do arquivo
print(os.path.join(os.getcwd() + os.sep + 'senhas.txt'))

# Retorna path do arquivo em sub-pasta
print(os.path.join(os.getcwd() + os.sep + 'documentos' + os.sep + 'musica.mp3')) 

caminho_senha = os.path.join(os.getcwd() + os.sep + 'senhas.txt')

# Obter o diretório de um path
print(os.path.dirname(caminho_senha)) 

# Obter arquivo de um path
print(os.path.basename(caminho_senha)) 

# Retorna se um diretório existe ou não
print(os.path.join(os.getcwd() + os.sep + 'documentos')) 

# Usado para se mover entre os dirtórios no python
os.chdir('') 

# Como criar arquivos e diretórios 

# Criar pastas ou diretórios 
os.mkdir('') 

# Criar pastas e sub-pastas mas tem que passar o separador que no caso é o os.sep
os.makedirs('') 

# Retorna se existe ou não um diretório com o nome passado
os.path.exists('') 

# Como criar e modificar arquivos

# 'w' -> Usado somente para escrever algo 
# 'a' -> Usado para acrescentar algo
# 'r' -> Usado somente para ler algo
# 'r+' -> Usado para ler e escrever algo

with open('celulares.txt','w') as arquivo:
    arquivo.write('Celular 1')

nomes = ['Luca', 'Carol', 'Jeff', 'Douglas']

with open('nome.txt', 'a', newline='') as arquivo:
    for nome in nomes:
        arquivo.write(nome + os.linesep)

numeros = [1, 2, 3, 4, 5, 6]

with open('numeros.txt', 'a', newline='') as arquivo:
    for numero in numeros:
        arquivo.write(str(numero) + os.linesep)

with open('numeros.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)

with open('numeros.txt', 'r+') as arquivo:
    for linha in arquivo:
        print(linha)
    arquivo.write('9000')

# Copia o arquivo de um lugar para o outro
shu.copy(src=os.getcwd() + os.sep + 'fotos' + os.sep + 'foto1.jpg', dst=os.getcwd() + os.sep + 'backup') 

# Copia todos os arquivos de uma pasta para a outra
shu.copytree(src=os.getcwd() + os.sep + 'fotos',dst=os.getcwd() + os.sep + 'fotos backup')

# Para mover arquivos entre os diretórios 
shu.move(src = os.getcwd() + os.sep() + 'fotos', dst = os.getcwd() + os.sep + 'backup')

# Para apagar um pasta e seus arquivos 
shu.rmtree(os.getcwd() + os.sep + 'musicas')

# Para compactar um arquivo (nome_do_arquivo_quando_for_compactado, formato para compactar os arquivos, o caminho da pasta que vai ser compactada)
shu.make_archive('backup_fotos', 'zip', os.getcwd() + os.sep + 'fotos')

# Para compactar todos os arquivos é só passar o diretório atual 
shu.make_archive('backup_fotos', 'zip', os.getcwd())

# Para descompactar uma pasta (nome_do_arquivo_compactado, local que vai ser descompactado)
shu.unpack_archive('backup_vs_code',os.getcwd() + os.sep + 'backup_vs_code')


