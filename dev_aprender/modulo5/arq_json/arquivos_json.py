# Arquivo JSON

import json
from pathlib import Path

""" carros = [
    {"Marca": "Nissan", "Preço": 45.000, "Cor": "Azul"},
    {"Marca": "Ford", "Preço": 75.000, "Cor": "Branco"},
    {"Marca": "BMW  ", "Preço": 117.000, "Cor": "Preto"},
]

carros_json = json.dumps(carros)
Path('carros.json').write_text(carros_json) """

""" arquivo_carros_json = Path('carros.json').read_text()
arquivo_json = json.loads(arquivo_carros_json)
print(arquivo_json[0]['Marca'] + ' ' + str(arquivo_json[0]['Preço'])) """

arquivo_pikachu_json = Path('pikachu.json').read_text()
arquivo_json = json.loads(arquivo_pikachu_json)

print(arquivo_json['abilities'][1]['ability']['name'])