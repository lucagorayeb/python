import webbrowser
import threading
import time

def baixar_fotos(site):
    print(f'Baixando foto do site {site}')

def navegando_ate_site(site):
    print(f'Navegando até o {site}')

thread = threading.Thread(target=baixar_fotos, args=('https://facebook.com', ), daemon=True)
thread.start()
navegando_ate_site('https://facebook.com')
thread.join()
