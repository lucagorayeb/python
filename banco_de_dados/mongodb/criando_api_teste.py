from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime
from pymongo import MongoClient

app = Flask(__name__)
con = MongoClient('mongodb://localhost:27017/')
db = con.get_database("teste_clinica")
colecao = db.get_collection('Pacientes')
CORS(app)

@app.route('/pacientes')
def obter_dados():
    dados = list(colecao.find())
    return jsonify(dados)