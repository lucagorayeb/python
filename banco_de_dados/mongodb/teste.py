from datetime import datetime, timedelta


data_string = "29/06/2015"
data = datetime.strptime(data_string, "%d/%m/%Y")
idade = (datetime.now() - data).days / 365
idade_formatada = int(f'{idade:.0f}')

print(type(idade_formatada))
