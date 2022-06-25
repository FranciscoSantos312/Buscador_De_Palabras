import csv
import re


frase = """ """.lower()
frasex = re.sub("’", "", frase)
frase2 = frasex.split(" ")
archivo = open("bd2022.csv", encoding="utf8")
archivo2 = archivo.read()
for frase3 in frase2:
    if frase3 not in  archivo2:
        print(frase3)

        

