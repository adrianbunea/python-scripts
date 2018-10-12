import string
from random import randrange

def filtreaza_regula_productie(caracter, regula_productie):
        if caracter in regula_productie[0]:
            return True
        else:
            return False

neterminale = ['E','T','F']
terminale = ['a','+','*','(',')']
start = 'E'
reguli_productie = [('E','E+T'),('E','T'),('T','T*F'),('T','F'),('F','a'),('F','(E)')]

sir = start
# while len(sir) < 60:
#     for caracter in sir:
#         if caracter in neterminale:
#             lista_filtrata = filter(filtreaza_reguli_productie(caracter), reguli_productie)
while len(sir) < 60:           
    for i in range(0, len(sir)):
        caracter = sir[i]
        if caracter in neterminale:
            lista_filtrata = ""
            for regula in reguli_productie:
                if caracter in regula[0]:
                    lista_filtrata = lista_filtrata + caracter
                    index = randrange(0,len(lista_filtrata))
                    sir = sir.replace(sir[i],lista_filtrata[index])

print(sir)