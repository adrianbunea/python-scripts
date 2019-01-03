from Functii import citeste_fisier
import argparse
import csv

stanga, dreapta = 0, 1

parser = argparse.ArgumentParser()
parser.add_argument("nume_fisier", help="alege un fisier text din care sa fie citita gramatica utilizata")
args = parser.parse_args()


def genereaza_substitutie(caractere):
	substitutie_posibila = ()
	for regula in reguli_productie:
		if caractere in regula[stanga]:
			substitutie_posibila = regula
			return substitutie_posibila
		return None



def INC(regula_productie):
	global neterminale
	global reguli_productie
	reguli_productie_copie = reguli_productie

	index_regula = reguli_productie.index(regula_productie)
	del(reguli_productie[index_regula])

	INC = [] # lista de reguli de productie, incepe cu prima
	regula_productie = (regula_productie[stanga], "." + regula_productie[dreapta])
	INC.append(regula_productie)
	print(INC[0])
	# while any(terminal in regula_productie[dreapta] for terminal in neterminale):

	for regula_productie in INC:
		for sir in reguli_productie[stanga]:  # verifica fiecare caracter de dupa punct daca este in INC
			index = regula_productie[dreapta].index('.') # obtine indexul punctului in regula de productie curenta
			ceva = regula_productie[dreapta]
			if regula_productie[dreapta].find(sir, index):
				# TREBUIE SA SCHIMB SI REGULA_PRODUCTIE DE STANGA
				substitutie = genereaza_substitutie(sir)
				if substitutie is not None:
					index_regula = reguli_productie.index(substitutie)
					del reguli_productie[index_regula]

					regula_productie = (regula_productie[stanga].replace(regula_productie[stanga], substitutie[stanga]), regula_productie[dreapta].replace(sir, substitutie[dreapta], 1))
					INC.append(regula_productie)
					print(regula_productie)

	reguli_productie = reguli_productie_copie
	return regula_productie

def URM():
	return

def SALT():
	return

# START
gramatica = citeste_fisier(args.nume_fisier)
neterminale = gramatica["neterminale"]
terminale = gramatica["terminale"]
start = gramatica["start"]
reguli_productie = gramatica["reguli_productie"]

# for regula_productie in reguli_productie:
# 	INC(regula_productie)
INC(reguli_productie[0])




