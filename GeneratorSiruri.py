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
            lista_optiuni = []
            for regula in reguli_productie:
                if caracter in regula[0]:
                    regula_posibila = regula[1]
                    lista_optiuni.append(regula_posibila)
                    index = randrange(0,len(lista_optiuni))
            sir = sir.replace(sir[i],lista_optiuni[index])

print(sir)
print(len(sir))