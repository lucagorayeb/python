
from flask import Flask, jsonify, request
from banco_de_dados.estrutura_de_bd import Autor, app, db


@app.route('/')
def bem_vindo():
    mensagem = 'bem vindo a está api'
    return mensagem

@app.route('/autores')
def obter_autores():
    autores = Autor.query.all()
    lista_de_autores = []
    for autor in autores:
        autor_atual = {}
        autor_atual['id_autor'] = autor.id_autor
        autor_atual['nome'] = autor.nome
        autor_atual['email'] = autor.email
        lista_de_autores.append(autor_atual)
    
    return jsonify ({'autores':lista_de_autores})

@app.route('/autores/<int:id_autor>',methods=['GET'])
def obter_autor_por_id(id_autor):
    pass

@app.route('/autores', methods=['POST'])
def novo_autor():
    pass

@app.route('/autores/<int:id_autor>',methods=['PUT'])
def alterar_autor(id_autor):
    pass

@app.route('/autores/<int:id_autor>',methods=['DELETE'])
def excluir_autor(id_autor):
    pass

app.run(port=5000, host='localhost', debug=True)