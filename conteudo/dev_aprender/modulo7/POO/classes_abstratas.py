# Classes Abstratas
# Criar um contrato (esqueleto) -> Que deve ser implementado na classe que a herda

from abc import ABC,abstractmethod

class Monitor(ABC):
    def aumentar_claridade(self, quantidade):
        pass

    def reduzir_clariade(self, quantidade):
        pass

class MonitorFullHd(Monitor):
    def aumentar_claridade(self, quantidade):
        print(f'A claridade foi aumentada em {quantidade}')
        
    def reduzir_clariade(self, quantidade):
        print(f'A claridade foi reduzida em {quantidade}')

monitor = MonitorFullHd()
monitor.aumentar_claridade(10)
monitor.reduzir_clariade(7)