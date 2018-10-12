import string
from random import randrange

neterminale = ['E','T','F']
terminale = ['a','+','*','(',')']
start = 'E'
reguli_productie = [('E','E+T'),('E','T'),('T','T*F'),('T','F'),('F','a'),('F','(E)')]

sir = start
lungime_sir = len(sir)

while lungime_sir < 60:  
    if all([caracter not in sir for caracter in neterminale]):
        break
    lungime_sir = len(sir)     
    for i in range(0, lungime_sir):
        caracter = sir[i]
        if caracter in neterminale:
            lista_filtrata = []
            for regula in reguli_productie:
                if caracter in regula[0]:
                    substitutie = regula[1]
                    lista_filtrata.append(substitutie)
                    index = randrange(0,len(lista_filtrata))
                    sir = sir.replace(sir[i],lista_filtrata[index])

print(sir)