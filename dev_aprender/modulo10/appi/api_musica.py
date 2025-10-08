from flask import Flask, jsonify, request

app = Flask(__name__)

musicas = [
    {
        'título': 'Dream on',
        'Banda': 'Aerosmith'
    },

    {
        'título': 'Like a Stone',
        'Banda': 'Audioslave'
    },

    {
        'título': 'Black summer',
        'Banda': 'Red Hot Chili Peppers'
    },
]

# GET - http://localhost:5000/
@app.route('/')
def obter_musicas():
    return jsonify(musicas)

# GET com id - http://localhost:5000/musicas/1
@app.route('/musicas/<int:indice>', methods=['GET'])
def obter_musica_por_id(indice):
    return jsonify(musicas[indice],200)

# POST - http://localhost:5000
@app.route('/musicas',methods=['POST'])
def nova_musica():
    musica = request.get_json()
    musicas.append(musica)
    return jsonify(musica, 200)

# PUT - http://localhost:5000/musicas/0
@app.route('/musicas/<int:indice>', methods=['PUT'])
def alterar_musica(indice):
    musica_alterada = request.get_json()
    musicas[indice].update(musica_alterada)
    return jsonify(musicas[indice],200)

# DELETE - http://localhost:5000/musicas/0
@app.route('/musicas/<int:indice>', methods=['DELETE'])
def deletar_musica(indice):
    try:
        if musicas[indice] is not None:
            del musicas[indice]
            return jsonify(f'Foi excluido a musica {musicas[indice]}', 200)
    except:
        return jsonify('Não foi possível encontrar a postagem para a exclusão', 404)
    
app.run(port=5000, host='localhost', debug=True)