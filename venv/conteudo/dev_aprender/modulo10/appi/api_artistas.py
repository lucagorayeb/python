from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def bem_vindo():
    mensagem = 'bem vindo a está api'
    return mensagem


@app.route('/artistas')
def obter_autores():
    with sqlite3.connect('artistas.db') as conexao:
        conexao.row_factory = sqlite3.Row
        sql = conexao.cursor()
        bandas = sql.execute('select * from banda;').fetchall()
        lista_bandas = []
        for banda in bandas:
            lista_bandas.append(dict(banda))
    return jsonify(lista_bandas)

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