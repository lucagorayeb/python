#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : orm_slqalchemy.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 15/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session


"""
    O argumento principal passado para o create_engine é uma url que indica 3 coisas:

    1 - O tipo de banco de dados que vai ser usado. Nesse caso vai ser o sqlite que vai ser 
        passado para um objeto chamado dialect.

    2 - O tipo de DBAPI que vai ser usada pelo SQLAlchemy. Nesse caso é o pysqlite. Caso nenhum
        driver de DBAPI seja fornecido o SQLAlchemy vai usar um padrão.

    3 - Como vai ser armazenado a database. Nesse caso é passado a frase /:memory que significa
        que vai rodar somente na memória e não vai precisar de um servidor ou de um arquivo.
    
    A create_engine não retorna um conexão com o banco. O SQLAlchemy usa um padrão de arquitetura
    chamado de lazy initialization que algo só inicializado quando um tarefa é executada.
"""
engine = create_engine("sqlite+pysqlite:///:memory", echo=True)

"""
    O proposito da engine é promover um objeto de conexão ao banco de dados. Quando a conexão 
    é estabelecida é aberto uma forma de todos os objetos de conexão interagirem com o banco de dados.
    Para evitar isso é usado um contexto e um modelador de contexto que é o 'with'
"""
""" with engine.connect() as conn:
    result = conn.execute(text("select 'Hello world.'"))
    print(result.all()) """

# Commit as you go 
""" with engine.connect() as conn:
    conn.execute(text("CREATE TABLE teste (id INTEGER NOT NULL, nome TEXT NOT NULL);"))
    conn.execute(text("INSERT INTO teste (id, nome) VALUES (:id, :nome)"), 
                    [{"id": 1, "nome": 'Luca'}, {"id": 2, "nome": 'Larissa'}],
                )
    conn.commit() 

with engine.connect() as conn:
    result = conn.execute(text('SELECT * FROM teste;'))
    print(result.all())"""

# Begin once
""" with engine.begin() as conn:
    conn.execute(text("INSERT INTO teste (id, nome) VALUES (:id, :nome);"), 
                    [{"id": 3, "nome": 'Luana'}, {"id": 4, "nome": 'Pedro'}] 
                ) """

# 5 Formas de mostrar a mesma saída
""" with engine.connect() as conn:
    result = conn.execute(text('SELECT * FROM teste;'))
    for row in result:
        print(f"id: {row.id} nome: {row.nome}")
 
    
with engine.connect() as conn:
    result = conn.execute(text('SELECT * FROM teste;'))
    for id, nome in result:
        print(f"id: {id} nome: {nome}")

with engine.connect() as conn:
    result = conn.execute(text('SELECT * FROM teste;'))
    for row in result:
        print(f"id: {row[0]} nome: {row[1]}")

with engine.connect() as conn:
    result = conn.execute(text('SELECT * FROM teste;'))
    for row in result:
        nome = row.nome
        print(f"id: {row.id} nome: {nome}") 

with engine.connect() as conn:
    result = conn.execute(text('SELECT * FROM teste;'))
    for dict_row in result:
        id = dict_row.id
        nome = dict_row.nome
        print(f"id: {id} nome: {nome}") 

with engine.connect() as conn:
    result = conn.execute(text('SELECT * FROM teste WHERE nome != "Luca"'))
    for row in result:
        print(f"id: {row.id} nome: {row.nome}") """

# Usando o Session execute ao inves do connect execute 
stmt = text("SELECT * FROM teste WHERE id > :id ORDER BY nome, id")
with Session(engine) as session:
    result = session.execute(stmt, {"id": 0})
    for row in result:
        print(f"id: {row.id} nome: {row.nome}")

stmt = text("UPDATE teste SET nome = :nome WHERE id = :id")
with Session(engine) as session:
    result = session.execute(stmt, [{"nome": 'Luca Gorayeb', "id": 1}])
    session.commit()

stmt = text("SELECT * FROM teste")
with Session(engine) as session:
    result = session.execute(stmt)
    for row in result:
        print(f"id: {row.id} nome: {row.nome}")