# Processar VS Retornar
# Função que apenas processa dados
print('Olá')
# Funções que retornam dados

# Como escolher entre funções que processam VS retornam dados?
""" Eu vou precisar usar informação na lógica do meu programa ainda? Ou só preciso processar esse dado, mas não irei utilizar mais ele depois? """

def exibir_cotacao_do_dia(moeda):
    if moeda == 'usd':
        print(5.47)

exibir_cotacao_do_dia('usd')

def obter_cotacao_do_dia(moeda):
    if moeda == 'usd':
        return 5.47

cotacao = obter_cotacao_do_dia('usd')
if cotacao > 5:
    print('Investir em ações norte americanas')
else:
    print('Cotação não favorável')