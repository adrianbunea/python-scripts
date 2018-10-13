import string
from random import randrange

neterminale = ['E','T','F']
terminale = ['a','+','*','(',')']
start = 'E'
reguli_productie = [('E','E+T'),('E','T'),('T','T*F'),('T','F'),('F','a'),('F','(E)')]

sir = start
lungime_sir = len(sir)

while lungime_sir <= 60:  
# Se opreste cand sirul are 60 de caractere
    if any([caracter in sir for caracter in neterminale]):
        # Daca exista un caracter neterminal in sir parcurge sirul  
        for i in range(0, lungime_sir):
            caracter = sir[i]
            if caracter in neterminale:
                # daca gaseste un caracter in lista de neterminale, genereaza o 
                # lista cu optiunile cu care poate substitui caracterul
                lista_optiuni = []
                for regula in reguli_productie:
                    # testeaza fiecare regula din regulile de productie
                    if caracter in regula[0]:
                        # daca caracterul se regaseste in partea stanga a regulii (regula[0]) 
                        # atunci e marcata drept candidat si adaugata in lista de optiuni
                        regula_posibila = regula[1]
                        lista_optiuni.append(regula_posibila)
                # se alege aleatoriu una dintre regulile posibile
                index = randrange(0,len(lista_optiuni))
                # daca dupa ce adauga noile caractere sirul devine mai lung de 60 iese din loop
                if lungime_sir + len(lista_optiuni[index])-1 > 60:
                    for j in range(0, lungime_sir):
                        caracter = sir[i]
                        if caracter in neterminale:
                            sir = sir.replace(sir[i],'')
                    break
                # se inlocuieste caracterul neterminal cu grupul de caractere din partea dreapta a regulii
                sir = sir.replace(sir[i],lista_optiuni[index])
                # se incrementeaza lungimea sirului cu lungimea caracterelor adaugate 
                # si se scade 1 pentru caracterul scos
                lungime_sir += len(lista_optiuni[index])-1

# in cazul in care lungimea sirului devine 59 dar inca nu s-au inlocuit toate caracterele neterminale, 
# acestea sunt inlocuite cu alte caractere terminale respectand regulile de productie
# WIP

print("Sir: " + str(sir))
print("Sirul are " + str(len(sir)) + " caractere.")