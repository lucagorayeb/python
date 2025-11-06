from datetime import datetime
from pymongo import MongoClient
from enums import Sexo

con = MongoClient('mongodb://localhost:27017/')
db = con.get_database("teste_clinica")
colecao = db.get_collection('Pacientes')

data_string = "29/06/2005"
data = datetime.strptime(data_string, "%d/%m/%Y")
dados = {
    "Nome": "Luca", 
    "DataNascimento": data, 
    "CPF": "023.107.662-24",
    "RG": "023.107.662-24",
    "Sexo": Sexo.masculino.value
}
colecao.insert_one(dados)
print(f'{list(colecao.find())}')


