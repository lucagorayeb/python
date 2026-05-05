from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui as pg
import time
import re

driver = webdriver.Chrome()
driver.get("https://google.com/mail")
time.sleep(2)

def fazer_login_gmail():
    elem = driver.find_element(By.NAME, "identifier")
    time.sleep(2)

    elem.send_keys("luca.gorayeb@tjro.jus.br", Keys.ARROW_DOWN)
    time.sleep(2)

    clicar = driver.find_element(By.CSS_SELECTOR,"button.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.LQeN7.BqKGqe.Jskylb.TrZEUc.lw1w4b")
    clicar.click()
    time.sleep(2)

    elem = driver.find_element(By.NAME, "Passwd")
    elem.send_keys("g0ml$5@9ks!", Keys.ARROW_DOWN)
    time.sleep(2)

    clicar = driver.find_element(By.CSS_SELECTOR,"#passwordNext > div > button")
    clicar.click()
    time.sleep(30) 

def mandar_mensagem_para_servidores(servidores):

    for servidor in servidores:

        clicar = driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/div/div[2]/div[1]/div[2]/div[1]")
        clicar.click()
        time.sleep(3)

        elem = driver.find_element(By.XPATH, '//*[@id="gs_lc50"]/input[1]')
        elem.send_keys(servidor)
        time.sleep(3)
        elem.send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        elem.send_keys(Keys.ENTER)
        time.sleep(3)

        pg.typewrite("Bom dia, eu trabalho da STIC, na DISUS dentro da SEAT. Foi identificado que o mini PC do(a) senhor(a) necessita atualizar para o Windows 11. Vou precisar agendar em momento oportuno para formatar o seu computador institucional, de acordo com a disponibilidade que o senhor(a) possuir, e atualizar para corrigir o problema. Esse processo visa regularizar os computadores para promover maior seguridade para o TJRO. Informe seu local de trabalho, andar ,uma data e uma hora para ser feito esse procedimento. Todos os servidores que receberem essa mensagem devem fazer devem ter seus computadores formatados. Caso tenha alguma problema, consulte o SEI 0007581-36.2023.8.22.8000, despacho 59323.")
        time.sleep(3)
        pg.press('enter')
        time.sleep(3) 

def fazer_o_vetor_servidores():
    nomes = []
    with open('arquivo.txt', 'r', encoding="utf-8") as arquivo:
        for linha in arquivo:
            formatacao1 = re.sub(r',.+', '', linha)
            formatacao2 = re.sub(r'CN=', '', formatacao1)
            formatacao3 = re.sub(r'\n', '', formatacao2)
            nomes.append(formatacao3)
        return nomes

servidores = fazer_o_vetor_servidores()

fazer_login_gmail()
mandar_mensagem_para_servidores(servidores)









