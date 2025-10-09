from csv import DictReader, DictWriter

with open('informações.csv', 'r', newline='', encoding='utf-8') as arquivo_original:
    dados_originais = DictReader(arquivo_original)
    infos = list(dados_originais)
    with open('informações_v2.csv', 'w', newline='', encoding='utf-8') as novo_arquivo:
        cabecalho = ['nome','idade','altura']
        csv_writer = DictWriter(novo_arquivo, fieldnames=cabecalho)
        csv_writer.writeheader()
        for info in infos:
            csv_writer.writerow({
                'nome': info["nome"],
                'idade': info["idade"],
                'altura': info["altura"]  + 'cm'
            })