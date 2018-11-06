# from Functii import *

import csv

lista = []

with open('TabelGramatica.csv', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    # next(reader)
    lista = [line for line in reader]
        
for line in lista:
    print(line)

print(lista[0]['id'])