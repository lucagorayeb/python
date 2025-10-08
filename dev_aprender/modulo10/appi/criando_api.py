# Minha primeira API - Flask 

# Flask 
from flask import Flask, jsonify, request
app = Flask(__name__)
postagens = [
    {
        'título': 'Minha Hitória',
        'autor' : 'Amanda Dias'
    },

    {
        'título': 'Novo Dispositivo Sony',
        'autor' : 'Howard Stringer'
    },

    {
        'título': 'Lançamento do Ano',
        'autor' : 'Jeff Bezos'
    },

]

# Rota padrão - GET http://localhost:5000/
@app.route('/')
def obter_postagens():
    return jsonify(postagens)

# Rota - GET com id http://localhost:5000/postagem/1
@app.route('/postagem/<int:indice>', methods=['GET'])
def obter_postagem_por_id(indice):
    return jsonify(postagens[indice], 200)

# Rota - Criar uma nova postagem - POST
@app.route('/postagem',methods=['POST'])
def nova_postagem():
    postagem = request.get_json()
    postagens.append(postagem)
    return jsonify(postagem, 200)

# Rota - Alterar uma postagem existente - PUT http://localhost:5000//postagem/0
@app.route('/postagem/<int:indice>', methods=['PUT'])
def alterar_postagem(indice):
    postagem_alterada = request.get_json()
    postagens[indice].update(postagem_alterada)
    return jsonify(postagens[indice],200)

# Rota - Deletar uma postagem - DELETE - http://localhost:5000//postagem/0
@app.route('/postagem/<int:indice>',methods=['DELETE'])
def excluir_postagem(indice):
    try:
        if postagens[indice] is not None:
            del postagens[indice]
            return jsonify(f'Foi exluido a postagem {postagens[indice]}',200)
    
    except:
       return jsonify('Não foi possível encontrar a postagem para a exclusão',404)


app.run(port=5000, host='localhost', debug=True)

