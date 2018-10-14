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

def citeste_fisier(nume_fisier):
    gramatica = open(nume_fisier, 'r')
    gramatica = gramatica.read()

    global neterminale
    neterminale = gramatica[gramatica.find("\nneterminale = ")+15 : gramatica.find("\nterminale")]
    neterminale = neterminale[neterminale.find('[\'')+2: neterminale.find('\']')]
    neterminale = neterminale.split('\',\'')

    global terminale
    terminale = gramatica[gramatica.find("\nterminale = ")+13 : gramatica.find("\nstart")]
    terminale = terminale[terminale.find('[\'')+2: terminale.find('\']')]
    terminale = terminale.split('\',\'')

    global start
    start = gramatica[gramatica.find("\nstart = ")+9 : gramatica.find("\nreguli_productie")]
    start = start.strip('\'')

    global reguli_productie
    reguli_productie = gramatica[gramatica.find("\nreguli_productie = ")+20 :]
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

print("Sir: " + sir)
print("Sirul are " + str(len(sir)) + " caractere.")