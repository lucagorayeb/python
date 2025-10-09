# Variáveis de uma classe 
class Computador:
    sistema_operacional = 'Windows 11' # Variável de classe
    def __init__(self, marca, quantidade_ram, placa_de_video):
        self.marca = marca # Variávei instaciadas da classe
        self.memoria_ram = quantidade_ram
        self.placa_de_vedeo = placa_de_video

    def ligar(self):
        print('Estou ligando o computador')

# Para altera uma variável eu preciso instancia-la
computador = Computador('Dell', '8gb', 'Nvidia')
computador.marca = 'Asus'
print(computador.marca)