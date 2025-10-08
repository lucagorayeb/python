import webbrowser
import threading
import time
import random

def navegar_ate_site(site, produto):
    print(f'Entrando no site {site} e pesquisando sobre {produto}')

produtos = ['celular', 'monitor', 'fone de ouvido', 'alto-falante', 'computador']
threads = []

for i in range(5):
    nova_thread = threading.Thread(target=navegar_ate_site, args=('https;//mercadolivre.com', produtos[i]))
    threads.append(nova_thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

