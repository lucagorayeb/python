from datetime import datetime

""" 
print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

# Criar uma data
lancamento_app = datetime(2025, 5, 11)
print(lancamento_app)

# Quero receber a data de lançamento do meu aplicativo
data_de_lacamento = datetime.strptime(input('Quando devemos lançar o aplicativo? '), '%d/%m/%Y')
print(data_de_lacamento)
print(type(data_de_lacamento))


# Calcular o intervalo entre datas
data_atual = datetime.now()
prazo = data_de_lacamento - data_atual
print(prazo.days) """

# Dias até o meu aniversário
b_day = datetime.strptime(input('Dia do seu anversário? '), '%d/%m/%Y')
data_atual = datetime.now()
dias_para_aniversario = b_day - data_atual
print(dias_para_aniversario.days)