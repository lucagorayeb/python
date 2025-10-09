# SQL - Structed Query Language
# db.sqlite3

import sqlite3


with sqlite3.connect('artistas.db') as conexao:
    # Criando um banco ou se conectanto a um banco já existente
    sql = conexao.cursor()
    # Rodar um comando SQL
    sql.execute('create table banda(nome text, estilo text, menbros interger);')
    # Exemplo de inserção em um banco de dados 
    sql.execute('insert into banda(nome, estilo, menbros) values ("Banda 1", "Rock", 3)')
    # Exemplo de usar dados da minha aplicação em um comando SQL
"""     nome = input('Digite o nome da banda: ')
    estilo = input('Digite o estilo da banda: ')
    quantidade_integrantes = int(input('Quantidade de integrantes da banda: '))

    sql.execute('insert into banda values(?,?,?)', [nome, estilo, quantidade_integrantes]) """

    # Salvando alterações no banco de dados 
conexao.commit()

    # Exibir dados no console python(terminal)
bandas = sql.execute('select * from banda;')
for banda in bandas:
    print(banda)