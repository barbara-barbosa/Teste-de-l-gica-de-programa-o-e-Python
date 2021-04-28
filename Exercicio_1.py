# -*- coding: utf-8 -*-
"""
@author: bbarbosa
"""
# Importar bibliotecas
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import requests


PATH = "C:\Program Files (x86)\chromedriver.exe" #localiza o webdriver instalado do path
driver = webdriver.Chrome(PATH)
driver.get("https://google.com.br")  # Acessar a URL especificada
search_bar = driver.find_element_by_name("q") #elemento da pagina de pesquisa do google
search_bar.clear() #limpar a barra de pesquisa
search_bar.send_keys("SulAmérica Investimento") #digitar sulamerica no campo de pesquisa
search_bar.send_keys(Keys.RETURN) #procurar o campo digitado
print(driver.current_url)
page = requests.get(driver.current_url)
driver.find_element_by_css_selector("div.r a h3").click() #acessar o site
driver.quit() #sair