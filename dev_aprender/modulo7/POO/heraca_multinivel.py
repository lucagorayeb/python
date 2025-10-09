# Herança Simples

class Usuario:
    def __init__(self, nome, salario, profissao):
        self.nome = nome
        self.salario = salario
        self.profissap = profissao

    def registrar_funcionario(self):
        print(f'Cadrastando usuário {self.nome}')

class Gestor(Usuario):
    def __init__(self, nome, salario, profissao,setor_responsavel):
        super().__init__(nome, salario, profissao)
        self.setor_responsavel = setor_responsavel
    
    def definir_setor(self, setor):
        print(f'Defininfo setor para {setor}')

usuario1 = Usuario('Camila', 5000, 'Analista de software')
gestor = Gestor('Roberta', 7000, 'Gestora', 'Gestão de Projetos')


# Herança Multinível 

# 1° Problema
""" class Veiculo:
    pass
class VeiculoDeRodas(Veiculo):
    quantidade_maxima_de_rodas = 2
    pass
class Carro(VeiculoDeRodas):
    pass
class CarroEletrico(Carro):
    pass
class CarroEletricoDuasPortas(CarroEletrico):
    pass """

# Herança Múltipla

class Pessoa:
    nome = 'Sou uma pessoa'

    def convidar(self):
        print('Olá sou uma pessoa, vamos ao evento?')

class Profissional:
    nome = 'Sou um profissional'
    def convidar(self):
        print('Olá sou uma profissional, vamos ao evento?')

class AtorProfissional(Pessoa, Profissional):
    pass

print(AtorProfissional.nome)
ator_profissional = AtorProfissional()
ator_profissional.convidar()

# MRO (Method Resolution Order)
print(AtorProfissional.mro())