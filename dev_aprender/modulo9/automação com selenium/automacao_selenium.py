import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# 1 - Criar um navegador webdriver
options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
# 2 - Navegar até um site 
driver.get('https://www.amazon.com.br/')
# 3 - Encontrar Elementos 
campo_caixa_pesquisa = driver.find_element(By.ID,"twotabsearchtextbox")
# 4 - Interagir com ele de alguma forma

# Clicar
campo_caixa_pesquisa.click()

# Digitar
campo_caixa_pesquisa.send_keys('Livros de TI')
botao_pesquisa = driver.find_element(By.ID,"nav-search-submit-button")
botao_pesquisa.click()

time.sleep(20)