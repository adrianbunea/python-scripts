from Functii import citeste_fisier
import argparse
import csv

stanga, dreapta = 0, 1

parser = argparse.ArgumentParser()
parser.add_argument("nume_fisier", help="alege un fisier text din care sa fie citita gramatica utilizata")
args = parser.parse_args()


def genereaza_substitutie(sir):
	for regula in reguli_productie:
		if sir in regula[stanga]:
			substitutie_posibila = regula
			return substitutie_posibila
	return None


def INC(INC):
	global reguli_productie
	copie_reguli_productie = reguli_productie[:]

	# indice_regula = reguli_productie.index(INC[0])
	# del reguli_productie[indice_regula]

	for regula_productie in INC:
		for regula in reguli_productie:
			sir = regula[stanga]
			dupa_punct = regula_productie[dreapta].split('.')[1]
			if dupa_punct != '':
				if dupa_punct[0].find(sir) != -1:
					substitutie = genereaza_substitutie(sir)
					indice_regula = reguli_productie.index(substitutie)
					del reguli_productie[indice_regula]
					substitutie = (substitutie[stanga], '.' + substitutie[dreapta])
					INC.append(substitutie)
					break
		if reguli_productie == []:
			break

	reguli_productie = copie_reguli_productie[:]
	return INC


def URM():
	return

def SALT(I_n, caracter):
	I = []
	for regula in I_n:
		inainte_de_punct = regula[dreapta].split('.')[0]
		dupa_punct = regula[dreapta].split('.')[1]
		if dupa_punct == '':
			# I += INC([regula])
			ceva = 0
		elif dupa_punct[0] == caracter:
			regula_noua = (regula[stanga], inainte_de_punct + dupa_punct[0] + '.' + dupa_punct[1:])
			I += INC([regula_noua])
	return I

# START
gramatica = citeste_fisier(args.nume_fisier)
neterminale = gramatica["neterminale"]
terminale = gramatica["terminale"]
start = gramatica["start"]
reguli_productie = gramatica["reguli_productie"]
reguli_productie.append(('S', start))

# for regula_productie in reguli_productie:
# 	INC(regula_productie)
# INC(reguli_productie[0])

reguli_cu_punct = []
for regula in reguli_productie:
	regula_cu_punct = (regula[stanga], '.' + regula[dreapta])
	reguli_cu_punct.append(regula_cu_punct)

C = []
I0 = INC([reguli_cu_punct[-1]])
C.append(I0)

for I_n in C:
	for caracter in neterminale + terminale:
		I = SALT(I_n, caracter)
		if I != []:
			if I not in C:
				C.append(I)

i = 0
for INC in C:
	print("I" + str(i))
	i += 1
	for regula in INC:
		print(regula)







