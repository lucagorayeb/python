# Como usar os 4 principais comandos(verbos) de uma API  
import requests
from pprint import pprint

# Get - Obter todos os recursos 
resultado_get = requests.get('https://jsonplaceholder.typicode.com/todos')
#pprint(resultado_get.json())

# Get com id - Obter recurso único 
resultado_get_com_id = requests.get('https://jsonplaceholder.typicode.com/todos/2')
#pprint(resultado_get_com_id.json())

# Post - Criar um novo recurso 
nova_tarefa = {'completed': False,
                'title': 'Lavar o carro',
                'userId': 1}

resultado_post = requests.post('https://jsonplaceholder.typicode.com/todos', nova_tarefa)
#pprint(resultado_post.json())

# Put - Serve para alterar um recurso existente
tarefa_alterada = {'completed': False,
                'title': 'Lavar a moto',
                'userId': 1}
resultado_put = requests.put('https://jsonplaceholder.typicode.com/todos/2', tarefa_alterada)
#pprint(resultado_put.json())

# Delete - Excluir um recurso 
resultado_delete = requests.delete('https://jsonplaceholder.typicode.com/todos/2')
pprint(resultado_delete.json())


