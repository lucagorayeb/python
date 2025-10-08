import webbrowser
import threading
import time
import random

def comentar(site, comentario):
    print(f'Entrando no site: {site}')
    print(f'Deixando um comentário: {comentario}')
    time.sleep(5)
    print(f'Dados processados no site: {site}')

comentarios = ['Olá', 'Legal', 'Muito Bom', 'Gostei', 'Excelente', 'Bom']
threads = []

for site in range(5):
    nova_thread = threading.Thread(target=comentar, args=(site, random.choices(comentarios)))
    threads.append(nova_thread)

for thread in threads:
    thread.start()
    #print(f'Iniciando {thread.name}')

for thread in threads:
    thread.join()
    #print(f'Finalizando {thread.name}')