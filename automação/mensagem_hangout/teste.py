import re

def fazer_o_vetor_servidores():
    nomes = []
    with open('arquivo.txt', 'r', encoding="utf-8") as arquivo:
        for linha in arquivo:
            formatacao1 = re.sub(r',.+', '', linha)
            formatacao2 = re.sub(r'CN=', '', formatacao1)
            formatacao3 = re.sub(r'\n', '', formatacao2)
            nomes.append(formatacao3)
        return nomes

servidores = fazer_o_vetor_servidores()
print(servidores)
