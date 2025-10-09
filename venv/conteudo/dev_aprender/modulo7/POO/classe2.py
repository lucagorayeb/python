# Metódos de uma classe -> ligar, desligar, exibir dados do computador
class Computador:
    def __init__(self, marca, quantidade_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = quantidade_ram
        self.placa_de_vedeo = placa_de_video

    def ligar(self): # O self é usado para acesssar qualquer parte dó código da classe
        print('Estou ligando o computador')
    
    def desligar(self):
        print('Estou desligando')
    
    def exibir_infos_do_computador(self):
        print(f'Computador da marca {self.marca}, com {self.memoria_ram} de memória ram e que usa a placa de vídeo {self.placa_de_vedeo}')

computador1 = Computador('Asus', '8gb', 'Nvidia')

computador1.ligar()
computador1.desligar()
computador1.exibir_infos_do_computador()

computador2 = Computador('Dell', '16gb', 'AMD')

computador2.ligar()
computador2.desligar()
computador2.exibir_infos_do_computador()