import string
from random import randrange

# Genereaza o lista de substitutii posibile pentru caracterul dat
def genereaza_lista_substitutii(caracter):
    lista_optiuni = []
    for regula in reguli_productie:
        if caracter in regula[0]:
            regula_posibila = regula[1]
            lista_optiuni.append(regula_posibila)
    return lista_optiuni

# Substituie caracterul neterminal. Incearca la intamplare substitutii, 
# daca substitutia ar face sirul mai lung de 60, este scoasa optiunea din
# lista de substitutii. Daca lista de substitutii devine goala atunci
# nu mai incearca sa subsitue si returneaza false. 
def substituie(caracter):
    lista_optiuni = genereaza_lista_substitutii(caracter)
    
    global sir
    while lista_optiuni != []:
        index = randrange(0,len(lista_optiuni))
        if len(sir) + len(lista_optiuni[index])-1 > 60:
            lista_optiuni.remove(lista_optiuni[index])
        else: 
            sir = sir.replace(caracter,lista_optiuni[index],1)
            return True
    return False

# Functia e folosita la finalul programului, in cazul in care sirul a ajuns 
# la 60 si mai are caractere neterminale aceasta le va scoate
def scoate_caractere_neterminale():
    global sir
    for caracter in sir:
        if caracter in neterminale:
            sir = sir.replace(caracter,'')

neterminale = ['E','T','F']
terminale = ['a','+','*','(',')']
start = 'E'
reguli_productie = [('E','E+T'),('E','T'),('T','T*F'),('T','F'),('F','a'),('F','(E)')]

sir = start
lungime_sir = len(sir)
   
substitutie = True

while substitutie == True:
    substitutie = False
    for caracter in sir:
        if caracter in neterminale:
           substitutie = substituie(caracter)

# scoate_caractere_neterminale()

print("Sir: " + sir)
print("Sirul are " + str(len(sir)) + " caractere.")