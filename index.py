from PyPDF2 import PdfReader, PdfWriter
from icecream import ic
from math import trunc, ceil 
import csv
import os
    
if not os.path.exists("./resultado"):
    os.mkdir('resultado')

archivo= PdfReader(open('./archivo.pdf','rb'))
pages=len(archivo.pages)
size=1
total_paginas=pages/size
paginas=trunc(total_paginas)
rest=ceil((total_paginas-paginas)* size)
lastpage=pages-rest
lenIndex=len(str(paginas))




lista_nombre =[]
csv_filename = 'NOMBRES.csv'
with open(csv_filename, newline='') as f:
    reader = csv.reader(f, delimiter=',', quotechar='|')

    for row in reader:
       lista_nombre.append("".join(row))



def crearSeccion(frompage, topage, filename):
    newManual=PdfWriter()
    for page in range(frompage, topage):
        newManual.add_page(archivo.pages[page])
    with open(f'./resultado/{filename}.pdf','wb') as fManual:
        newManual.write(fManual)


def generateIndex(num,length):
    num=str(num)
    return '0'*(length-len(num))+num


for pagina in range(paginas):
    newSection=pagina*size 
    crearSeccion(newSection, newSection+size, lista_nombre[pagina])
if rest != 0:
    crearSeccion(lastpage, lastpage+rest,f'archivo_{generateIndex(paginas+1,lenIndex)}')
 