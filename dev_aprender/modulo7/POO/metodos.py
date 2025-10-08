# Metódos comuns
# Metódos da Classe(Class Methods)
# Metódos Estáicos(Static Methods)
class Computador:
    sistema_operacional = 'Windows 11' # Variável de classe
    def __init__(self, marca, quantidade_ram, placa_de_video):
        self.marca = marca # Variávei instaciadas da classe
        self.memoria_ram = quantidade_ram
        self.placa_de_vedeo = placa_de_video

    def exibir_infos_do_computador(self):
        print(self.marca, self.memoria_ram, self.placa_de_vedeo, self.sistema_operacional)

    @classmethod
    def computador_escritorio(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de Vídeo - Baixo Custo')
    
    @classmethod
    def computador_configuracao_pesado(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de Vídeo - Alto Nível')
    
    @staticmethod
    def roda_programas_pesados(memoria_ram):
        if memoria_ram >= 8:
            return True
        else:
            return False

print(Computador.roda_programas_pesados(10))


""" # Configurações para cliente de escritório 
computador1 = Computador.computador_escritorio('8gb')
# Configuração para clientes de trabalho pesado(jogos, vídeos, 3d)
computador2 = Computador.computador_configuracao_pesado('16gb')

computador1.exibir_infos_do_computador()
print('######################')
computador2.exibir_infos_do_computador() """