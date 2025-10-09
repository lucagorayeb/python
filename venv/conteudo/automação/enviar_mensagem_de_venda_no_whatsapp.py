from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import schedule

midias = []

def enviar_midias():
    for midia in midias:
        pass

""" schedule.every().day.at("15:00").do(mandar_mensagem_no_whatsapp)

while True:
    schedule.run_pending()
    time.sleep(1) """