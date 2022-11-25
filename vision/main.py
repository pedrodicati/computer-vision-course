import pandas as pd

from pytesseract import Output, image_to_string, image_to_data
from PIL import Image, ImageOps

# lendo imagem RGB
image = Image.open('01.jpeg')

# convertendo a imagem para escala de cinza
image_gray = ImageOps.grayscale(image)

# conversão dos valores da matriz em strings
text = image_to_string(image_gray)

# print(text)

dictionary = image_to_data(image_gray, output_type=Output.DICT)

# print(dictionary)

# salvando dados em um arquivo .csv
file_csv = pd.DataFrame.from_dict(dictionary)
file_csv.to_csv('data.csv', index=False, header=True)

# tratando os dados para a visualização correta e não interferência dos valores nulos e inexistentes

dict_clean = {}

for key in dictionary:
    list_clean = []

    # aqui pega a lista que é o valor da chave que esta sendo usada em key
    # ai gera um csv
    for indice, item in enumerate(dictionary[key]):
        if dictionary['conf'][indice] >= 50:
            list_clean.append(item)
    
    dict_clean[key] = list_clean

file_csv = pd.DataFrame.from_dict(dict_clean)
file_csv.to_csv('data_clean.csv', index=False, header=True)