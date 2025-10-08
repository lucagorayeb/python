import pyautogui as pg
import webbrowser as web
import time


group_name = 'Olx'
message = f'''Me chamo Luca Siqueira Assis Gorayeb de Mello e estou oferecendo meus trabalhos como desenvolvedor de sites e programas personalizados, automatizar processos e projetos sob demanda. Se tiver um problema de hardware,  instalo programas, formato computadores, atualizo e otimizo, valores conforme a demanda. Se tiver interesse, por favor me chamar no privado.'''

# Função que faz executar a tecla tab 
def chamar_tab(quantidade):
    for n in range(quantidade):
        pg.press('tab')
        time.sleep(5)

# Função que executar o comando enter
def chamar_enter():
    pg.press('enter')
    time.sleep(5)

# Função que abre o whatsApp e envia a mensagem 
def mandar_mensagem_no_whatsapp():
    web.open("https://web.whatsapp.com")
    width, height = pg.size()
    pg.click(width/2, height/2)
    chamar_tab(6)
    pg.typewrite(group_name)
    chamar_tab(2)
    chamar_enter()
    pg.typewrite(message, interval=0.0, logScreenshot=None, _pause=False)
    chamar_enter()

# Executa a função mandar_mensagem_no_whatsapp todo dia as 15 horas
#every().day.at("15:58").do(mandar_mensagem_no_whatsapp)

# Inicia o schedule 
#while True:
#    schedule.run_pending()
 #   time.sleep(1) 
