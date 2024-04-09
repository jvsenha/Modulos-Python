import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By



# Inicialize o driver do navegador (neste caso, Chrome)
nav = webdriver.Chrome()

# Abra a página da web
nav.get('https://diariotransparente.com.br/publicacoes/frame/spfernandopolispm')

# Encontre o link dentro de divs específicas usando XPath
primeiro_link = nav.find_element(By.XPATH, '//*[@id="publishPublishGroup"]/div[2]/div/div/article/div[1]/a')

# Clique no primeiro link
primeiro_link.click()

# Caminho para o diretório de download
download_dir = "C:/Users/joaos/Downloads"

# Obtenha a lista de arquivos antes do download
before = os.listdir(download_dir)

# Aguarde o download ser concluído
# Isso depende do tamanho do arquivo e da velocidade da sua conexão com a internet
time.sleep(10)

# Obtenha a lista de arquivos após o download
after = os.listdir(download_dir)

# Encontre a diferença entre as duas listas
change = set(after) - set(before)

# O nome do arquivo baixado é a diferença entre as duas listas
if len(change) == 1:
    file_name = change.pop()
    print(f"O arquivo baixado é {file_name}")
else:
    print("Mais de um arquivo ou nenhum arquivo foi baixado")

# Feche o navegador após o download ser concluído
nav.quit()
