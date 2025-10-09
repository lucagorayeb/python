from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
import time







def for_mensagem():
    for i in range(2):
        driver = webdriver.Chrome()

        driver.get("https://web.whatsapp.com/")
        time.sleep(30)

        elem = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div/div/div[1]/p')
        time.sleep(2)

        elem.send_keys("Gorayeb")
        time.sleep(2)
        elem.send_keys( Keys.ARROW_DOWN)
        elem.send_keys(Keys.ENTER)
        elem = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[3]/div[1]/p')
        time.sleep(2)
        elem.send_keys("Responde")
        i = i + 1


for_mensagem()