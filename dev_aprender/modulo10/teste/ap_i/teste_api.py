from flask import Flask, jsonify, request, make_response
import sqlite3
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

# Criar uma API flask
app = Flask(__name__)
# Criar uma instância 
app.config['SECRET_KEY'] = 'FSD2323f#$!SAH'
jwt = JWTManager(app)

@app.route('/login', methods=["GET"])
@jwt_required()
def login():
    usuario = get_jwt_identity()
    return jsonify(logged_in_as=usuario), 200

@app.route('/')
def bem_vindo():
    mensagem = 'bem vindo a está api'
    return mensagem


@app.route('/jogadores')
def obter_jogadores():
    con =  sqlite3.connect('banco_de_teste.db')
    sql = con.cursor()
    jogadores = sql.execute('SELECT * FROM jogadores;').fetchall()
    return jsonify(f'Lista de todos os jogadores: {jogadores}')
    # Para que mostre com a formatação é só usar 'jogador':lista_jogadores            

@app.route('/jogadores/<int:id_jogador>',methods=['GET'])
def obter_jogador_por_id(id_jogador):
    con = sqlite3.connect('banco_de_teste.db')
    sql = con.cursor()
    jogadores = sql.execute(f'SELECT * FROM jogadores WHERE id_jogador = {id_jogador};').fetchall()
    return jsonify(f'Jogador pesquisado: {jogadores}')

@app.route('/jogadores', methods=['POST'])
def novo_jogador():
    con = sqlite3.connect('banco_de_teste.db')
    sql = con.cursor()
    jogador = [(int(input("Id: ")), input("Nome: "), input("Time: ") )]
    sql.executemany('INSERT INTO jogadores VALUES (?,?,?)',jogador) 
    return jsonify("Jogador cadastrado com sucesso")

@app.route('/jogadores/<int:id_jogador>',methods=['PUT'])
def alterar_jogador(id_jogador):
    con =  sqlite3.connect('banco_de_teste.db')
    sql = con.cursor()
    sql.execute(f"UPDATE jogadores SET nome = '{input(" ")}', time = '{input(" ")}' WHERE id_jogador = {id_jogador}")      
    return jsonify("Jogador alterado com sucesso")

@app.route('/jogadores/<int:id_jogador>',methods=['DELETE'])
def excluir_jogador(id_jogador):
    con = sqlite3.connect('banco_de_teste.db')
    sql = con.cursor()
    sql.execute(f"DELETE FROM jogadores WHERE id_jogador = {id_jogador}")  
    return jsonify("Jogador deletado com sucesso")

app.run(port=5000, host='localhost', debug=True)