import string
from random import randrange

def sterge_lambda():
    global sir
    sir = sir.replace('lambda', '')

def genereaza_lista_substitutii(caracter):
    lista_optiuni = []
    for regula in reguli_productie:
        if caracter in regula[0]:
            regula_posibila = regula[1]
            lista_optiuni.append(regula_posibila)
    return lista_optiuni

def substituie(caracter):
    lista_optiuni = genereaza_lista_substitutii(caracter)

    global sir
    sterge_lambda()
    while lista_optiuni != []:
        index = randrange(0,len(lista_optiuni))
        if len(sir) + len(lista_optiuni[index])-1 > 60:
            lista_optiuni.remove(lista_optiuni[index])
        else: 
            sir = sir.replace(caracter,lista_optiuni[index],1)
            return True
    return False

def citeste_fisier(nume_fisier):
    gramatica = open(nume_fisier, 'r')
    gramatica = gramatica.read().replace("\n", '')

    global neterminale
    neterminale = gramatica[gramatica.find("neterminale = ")+14 : gramatica.find("terminale", gramatica.find("neterminale = ")+14)]
    neterminale = neterminale[neterminale.find('[\'')+2: neterminale.find('\']')]
    neterminale = neterminale.split('\',\'')

    global terminale
    terminale = gramatica[gramatica.find("terminale = ", gramatica.find("neterminale = ")+14)+12 : gramatica.find("start")]
    terminale = terminale[terminale.find('[\'')+2: terminale.find('\']')]
    terminale = terminale.split('\',\'')

    global start
    start = gramatica[gramatica.find("start = ")+8 : gramatica.find("reguli_productie")]
    start = start.strip('\'')

    global reguli_productie
    reguli_productie = gramatica[gramatica.find("reguli_productie = ")+19 :]
    reguli_productie = reguli_productie[reguli_productie.find('[(')+1: reguli_productie.find(')]')]
    reguli_productie_temp = reguli_productie.split('),(')
    reguli_productie = []
    for regula_temp in reguli_productie_temp:
        regula = []
        regula_temp = regula_temp.strip('\'')
        regula.append(regula_temp.split('\' \'')[0])
        regula.append(regula_temp.split('\' \'')[1])
        regula = tuple(regula)
        reguli_productie.append(regula)

neterminale = ""
terminale = ""
start = ''
reguli_productie = ""
citeste_fisier("Gramatica.txt")

sir = start
lungime_sir = len(sir)
   
substitutie = True

while substitutie == True:
    substitutie = False
    for caracter in sir:
        if caracter in neterminale:
           substitutie = substituie(caracter)

sterge_lambda()

print("Sir: " + sir)
print("Sirul are " + str(len(sir)) + " caractere.")