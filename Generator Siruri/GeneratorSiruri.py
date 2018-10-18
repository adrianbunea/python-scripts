import string
import argparse
from random import randrange

parser = argparse.ArgumentParser()
parser.add_argument("nume_fisier", help = "alege un fisier text din care sa fie citita gramatica utilizata")
args = parser.parse_args()

stanga, dreapta = 0, 1

def sterge_lambda(sir):
    sir = sir.replace('_', '')
    return sir

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

def citeste_fisier(nume_fisier):
    gramatica = open(nume_fisier, 'r').read().replace('\n', '')

    neterminale = gramatica[gramatica.find("NETERMINALE:"): gramatica.find("TERMINALE:", gramatica.find("NETERMINALE:")+len("NETERMINALE:"))]
    gramatica = gramatica.replace(gramatica[gramatica.find("NETERMINALE:"): gramatica.find("TERMINALE:", gramatica.find("NETERMINALE:")+len("NETERMINALE:"))], '')
    neterminale = neterminale.replace("NETERMINALE:", '')
    neterminale = neterminale.split(' ')

    terminale = gramatica[gramatica.find("TERMINALE:") : gramatica.find("START:", gramatica.find("TERMINALE:")+len("TERMINALE:"))]
    gramatica = gramatica.replace(gramatica[gramatica.find("TERMINALE:") : gramatica.find("START:", gramatica.find("TERMINALE:")+len("TERMINALE:"))], '')
    terminale = terminale.replace("TERMINALE:", '')
    terminale = terminale.split(' ')

    start = gramatica[gramatica.find("START:") : gramatica.find("REGULI_PRODUCTIE:", gramatica.find("START:")+len("START:"))]
    start = start.replace("START:", '')

    reguli_productie = []
    reguli_productie_temp = gramatica[gramatica.find("REGULI_PRODUCTIE:"):]
    reguli_productie_temp = reguli_productie_temp.replace("REGULI_PRODUCTIE:", '')
    reguli_productie_temp = reguli_productie_temp.split(';')
    for regula in reguli_productie_temp:
        termen_stanga = regula.split('->')[stanga].replace(' ','')
        termeni_dreapta = regula.split('->')[dreapta].replace(' ', '').split('|')
        for termen in termeni_dreapta:
            reguli_productie.append((termen_stanga, termen))

    # gramatica = tuple(neterminale,terminale,start,reguli_productie)
    gramatica = {"neterminale" : neterminale, "terminale" : terminale, "start" : start, "reguli_productie" : reguli_productie}
    return gramatica

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