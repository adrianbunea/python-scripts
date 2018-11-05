from Functii import *

import string
import argparse
from random import randrange

parser = argparse.ArgumentParser()
parser.add_argument("nume_fisier", help = "alege un fisier text din care sa fie citita gramatica utilizata")
args = parser.parse_args()

sir = ""

def genereaza_lista_substitutii(caractere):
    lista_optiuni = []
    for regula in reguli_productie:
        if caractere in regula[stanga]:
            substitutie_posibila = regula[dreapta]
            lista_optiuni.append(substitutie_posibila)
    return lista_optiuni

def substituie(caractere):
    lista_optiuni = genereaza_lista_substitutii(caractere)

    global sir
    sir = sterge_lambda(sir)
    while lista_optiuni != []:
        index = randrange(0,len(lista_optiuni))
        if len(sir) + len(lista_optiuni[index])-1 > 60:
            lista_optiuni.remove(lista_optiuni[index])
        else: 
            sir = sir.replace(caractere,lista_optiuni[index],1)
            sir = sterge_lambda(sir)
            return True
    return False

# START
gramatica = citeste_fisier(args.nume_fisier)
neterminale = gramatica["neterminale"]
terminale = gramatica["terminale"]
start = gramatica["start"]
reguli_productie = gramatica["reguli_productie"]

sir = start
lungime_sir = len(sir)
   
substitutie = True

while substitutie == True:
    index = len(sir)
    substitutie = False
    for regula in reguli_productie:
        if sir.find(regula[stanga]) >= 0 and sir.find(regula[stanga]) < index:
            index = sir.find(regula[stanga])
            caractere = regula[stanga]
    if index < len(sir):
        substitutie = substituie(caractere)

sir = sterge_lambda(sir)

print("Sir: " + sir)
print("Sirul are " + str(len(sir)) + " caractere.")