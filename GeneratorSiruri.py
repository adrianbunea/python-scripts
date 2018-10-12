import string
import random

def filtreaza_reguli_productie(lista, caracter):
    for regula in lista:
        if regula[0] == caracter:
            return True
        else:
            return False

neterminale = {'E','T','F'}
terminale = {'a','+','*','(',')'}
start = 'S'
reguli_productie = [('E','E+T'),('E','T'),('T','T*F'),('T','F'),('F','a'),('F','(E)')]

sir = start
while len(sir) < 60:
    for caracter in sir:
        if caracter in neterminale:
            lista_filtrata = filter(filtreaza_reguli_productie(reguli_productie, caracter), reguli_productie)
            
Caracter = reguli_productie[0][0]
print(Caracter)