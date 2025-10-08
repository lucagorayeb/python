""" # Código solto

marca = input('Digite a marca do seu computador: ')
memoria = input('Digite a quantidade de memória ram: ')
placa = input('Digite qual a sua placa de vídeo: ')

print(f'Seu computador é da marca: {marca}')
print(f'Seu computador possui {memoria} de memória ram')
print(f'Seu computador possui uma placa de vídeo: {placa}')

# Funções

def exibit_infos_do_computador():
    marca = input('Digite a marca do seu computador: ')
    memoria = input('Digite a quantidade de memória ram: ')
    placa = input('Digite qual a sua placa de vídeo: ')

    print(f'Seu computador é da marca: {marca}')
    print(f'Seu computador possui {memoria} de memória ram')
    print(f'Seu computador possui uma placa de vídeo: {placa}')

exibit_infos_do_computador() 
 """
# Classe

class Computador:
    def __init__(self, marca, quantidade_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = quantidade_ram
        self.placa_de_vedeo = placa_de_video

# marca, memória ram, placa de vídeo
computador1 = Computador('Asus', '16gb', 'Nvidia')
print(computador1.marca)
print(computador1.memoria_ram)
print(computador1.placa_de_vedeo)

computador2 = Computador('Dell', '8gb', 'AMD')
print(computador2.marca)
print(computador2.memoria_ram)
print(computador2.placa_de_vedeo)
