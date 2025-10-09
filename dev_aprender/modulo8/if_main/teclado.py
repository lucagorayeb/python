from mouse import clicar

def digitar():
    print('Digitando')
    print(__name__)

if __name__ == '__main__': # Quando chamamos uma função como módulo a propriedade name recebe o nome do arquivo
    clicar()
    digitar()