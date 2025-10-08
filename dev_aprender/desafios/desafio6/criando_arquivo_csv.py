from csv import DictReader, DictWriter

with open('informações.csv', 'w', newline='',encoding='utf-8') as arquivo:
    cabecalho = ['nome','idade','altura']
    csv_writer = DictWriter(arquivo, fieldnames=cabecalho)
    csv_writer.writeheader()
    csv_writer.writerow({
        'nome': 'Mark',
        'idade': 25,
        'altura': '170'
    }),

    csv_writer.writerow({
        'nome': 'Carol',
        'idade': 19,
        'altura': '160'
    }),

    csv_writer.writerow({
        'nome': 'Robert',
        'idade': 65,
        'altura': '175'
    })