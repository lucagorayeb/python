from datetime import datetime
from pymongo import MongoClient
from enums import Sexo

con = MongoClient('mongodb://localhost:27017/')
db = con.get_database("teste_clinica")
colecao = db.get_collection('Pacientes')

data_string = "29/06/2005"
data = datetime.strptime(data_string, "%d/%m/%Y")
idade = (datetime.now() - data).days / 365
idade_formatada = int(f'{idade:.0f}')
dados = {
    "Nome": "Luca", 
    "DataNascimento": data, 
    "CPF": "023.107.662-24",
    "RG": "023.107.662-24",
    "Sexo": Sexo.masculino.value,
    "Numero": 69999558500 ,
    "Idade": idade_formatada,
    "NomeResponsavel": "",
    "NumeroResponsavel": "" ,
    "Endereco": [
        {"CEP": 76821051},
        {"Logradouro":"Avenida Prefeito Chiquilito Erse"},
        {"Numero": 4069},
        {"Bairro": "Industrial"},
        {"Cidade": "Porto Velho"},
        {"Estado": "Rondônia"}
    ]

}
colecao.insert_one(dados)

mostra = colecao.find()
print(list(mostra))

""" for dado in dados:
    for endereco in dados["Endereco"]:
        for end in endereco:
            print(f'{end}: {endereco[end]}')

    if dado == "Endereco" or dado == "DataNascimento" or idade_formatada < 18 or dado == "NomeResponsavel" or dado ==:
        
    if dado == "DataNascimento":
        data_formatada = dados[dado].strftime("%d/%m/%Y")
        print(f'{dado}: {data_formatada}')
    else:
        print(f'{dado}: {dados[dado]}')
        if idade_formatada < 18:
            colecao.update_one(
                {"Nome": "Luca"},
                {"$set":{"NomeResponsavel": "Pai", "NumeroResponsavel": 903}}
            )
            for res in dados["No"]:
                for responsaveis in res:
                    print(f'{responsaveis}: {res[responsaveis]}') """

        


