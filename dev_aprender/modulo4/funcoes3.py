def exibir_preco_nome_do_produto(nome, preco):
    print(f'{nome} está no valor de {preco} reais')

# Argumrntos posicionais
exibir_preco_nome_do_produto('Panela', 59.99) 

# Argumentos nomeados
exibir_preco_nome_do_produto(preco = 59.99, nome = 'Panela')

def gerar_objeto_personalizado(cor, *, altura, formato): # O * obrigato quem está na frente dele a ser nomeado
    print(f'O objeto tem a cor {cor}, a altura {altura} cm e o formato {formato}')

gerar_objeto_personalizado('preta', altura = 15, formato = 'vertical com a cabeça arredondada')