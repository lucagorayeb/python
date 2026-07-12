from selenium import webdriver
from selenium.webdriver.common.keys import Keys as key
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

driver = webdriver.Firefox()
driver.get("https://medium.com/codex/day-1-introduction-to-linux-5e7795be5d00")
elem = driver.find_element(By.TAG_NAME, "body")
time.sleep(100)
elem.send_keys(key.CONTROL + '+ a')
elem.send_keys(key.CONTROL + '+ c')
""" driver.perform(key.CONTROL, key.A) """
""" html_doc = response
print(html_doc)
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.get_text()) """
driver.close()

""" import requests


url = 'https://medium.com/codex/day-1-introduction-to-linux-5e7795be5d00'
response = requests.get(url)
print(response)

html_doc = response.text 
print(html_doc)

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.get_text()) """