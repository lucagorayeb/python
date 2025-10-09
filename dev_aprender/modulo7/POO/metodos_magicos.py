# Metods magicos

class Pessoa:
    def __init__(self):
        self.nome = 'Sou uma pessoa'
        self.habilidades = ['Habilidade 1', 'Habilidade 2', 'Habilidade 3']
    
    def __repr__(self):
        return 'Classe pessoa com proprieda nome e habilidade'
    
    def __len__(self):
        return len(self.habilidades)
    
    def __str__(self):
        return f'{self.nome} com as habilidades {self.habilidades}'
        
pessoa = Pessoa()
print(pessoa.nome)

print(repr(pessoa))
print(len(pessoa))