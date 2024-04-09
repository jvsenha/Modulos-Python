from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# Obtenha o caminho absoluto do diretório atual
dir_path = os.path.abspath(os.getcwd())

# Construa o caminho para o arquivo HTML
file_path = 'file://' + os.path.join(dir_path, 'exemple.html')

# Inicialize o driver do navegador (neste caso, Chrome)
nav = webdriver.Chrome()

# Abra o arquivo HTML
nav.get(file_path)

# Encontre o primeiro link na página
primeiro_link = nav.find_element(By.XPATH, '//a')

# Pegue o URL do primeiro link
url = primeiro_link.get_attribute('href')

print(url)  # Imprime o URL do primeiro link

button = nav.find_element(By.XPATH, '/html/body/button')

button.click()

# Encontre o primeiro link na página
primeiro_link = nav.find_element(By.XPATH, '//a')

# Pegue o URL do primeiro link
url = primeiro_link.get_attribute('href')

print(url)  # Imprime o URL do primeiro link

while True:
    pass
