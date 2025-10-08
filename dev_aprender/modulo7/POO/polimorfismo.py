# Polimorfismo 

class Carro:
    def ligar(self):
        print('Ligando o carro')

class Moto:
    def ligar(self):
        print('Ligando a moto')

def iniciar(veiculo):
    veiculo.ligar()

carro = Carro()
moto = Moto()

iniciar(carro)
iniciar(moto)

# Outra forma de polimorfismo

class Pessoa:
    def apresentar(self, nome, idade =  None, trabalho = None):
        if idade and trabalho != None:
            print(f'{nome} {idade} {trabalho}')
        elif idade != None:
            print(f'{nome} {idade}')
        elif trabalho != None:
            print(f'{nome} {trabalho}')
        else:
            print(nome)

pessoa = Pessoa()

pessoa.apresentar('Luca', 19, 'Desenvolvedor')
pessoa.apresentar('Luca', 19)
pessoa.apresentar('Luca','Desenvolvedor')
pessoa.apresentar('Luca')