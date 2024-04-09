import pytesseract
import cv2
import re
pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files\Tesseract-OCR\tesseract.exe"

#ler imagem
imagem = cv2.imread("cpf.jpg")

#pré-processamento da imagem
imagem_cpf_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)# deixar imagem em tons de cinza
#redmiensionar a imagem
imagem_cpf_cinza = cv2.resize(imagem_cpf_cinza, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
#extrair texto
texto= pytesseract.image_to_string(imagem_cpf_cinza, lang="por")

padrao= r"\d{3}\.\d{3}\.\d{3}-\d{2}"
cpf=re.findall(padrao, texto)
print(cpf)