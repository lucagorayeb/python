import os
import shutil as shu

""" def ler_arquivo():
    with open('csv_exemplo.csv') as arquivo:
        dados = arquivo.read()
        print(dados) """

""" 
def mover_arquivo():
    shu.move(src = 'C:' + os.sep + 'Users' + os.sep + 'lucag' + os.sep + 'Downloads' + os.sep + 'csv_exemplo.csv', dst = os.getcwd()) """

from csv import DictReader, DictWriter

# Ler um arquivo CSV
""" with open('csv_exemplo.csv') as arquivo:
    dados = DictReader(arquivo)
    for dado in dados:
        print(dado['OrderId'] + ' ' + dado['Age']) """

# Criar um arquivo CSV
""" with open('computadores.csv', 'w', newline='', encoding='utf-8') as arquivo:
    cabecalho = ['Marca', 'Preço', 'Ano de Lançamento']
    csv_writer = DictWriter(arquivo,fieldnames=cabecalho)
    csv_writer.writeheader()
    csv_writer.writerow({
        'Marca': 'Asus',
        'Preço': 2500,
        'Ano de Lançamento': 2010
    }),
    csv_writer.writerow({
        'Marca': 'Acer',
        'Preço': 3500,
        'Ano de Lançamento': 2015
    }),
    csv_writer.writerow({
        'Marca': 'Dell',
        'Preço': 4500,
        'Ano de Lançamento': 2014
    }), """

# Alterar um arquivo CSV
with open('computadores.csv','r', newline='', encoding='utf-8') as arquivo_original:
    dados_originais = DictReader(arquivo_original)
    computadores = list(dados_originais)
    with open('computadores_v2.csv', 'w', newline='', encoding='utf-8') as novo_arquivo:
        cabecalho = ['Marca', 'Preço', 'Ano de Lançamento']
        csv_writer = DictWriter(novo_arquivo,fieldnames=cabecalho) 
        csv_writer.writeheader()
        for computador in computadores:
            csv_writer.writerow({
                'Marca': computador["Marca"],
                'Preço': 'R$' + computador["Preço"],
                'Ano de Lançamento': computador["Ano de Lançamento"]
            })

