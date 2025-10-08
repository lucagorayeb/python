class HashTable:
    #Definindo o tamanho do vetor
    def __init__(self,size):
        self.table = [-1] * size # -1 indica posição vazia

    #Função hash básica: Módulo
    def hash_function(self, key):
        return key % len(self.table)

    #Inserção simples
    def insert(self, key):
        index = self.hash_function(key)
        self.table[index] = key

    #Exibir Table
    def display(self):
        for i, value in enumerate(self.table):
            print(f"Índice {i}: {value}")

#uso
ht = HashTable(10)
ht.insert(12)
ht.insert(33)
ht.insert(64)
#O número 15 não vai aparecer pq essa tabela não trata colisões
ht.insert(15)
ht.insert(25)
ht.display()