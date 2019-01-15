from Functii import citeste_fisier
import argparse
import csv

stanga, dreapta = 0, 1

parser = argparse.ArgumentParser()
parser.add_argument("nume_fisier", help="alege un fisier text din care sa fie citita gramatica utilizata")
args = parser.parse_args()


def urm(neterminal):
	URM = []
	for regula in reguli_productie:
		if neterminal in regula[dreapta]:
			parte_dreapta = regula[dreapta].split(neterminal,1)[1]
			if parte_dreapta == '':
				URM += urm(regula[stanga])
			else:
				ceva = terminale[:]
				ceva.append('$')
				if parte_dreapta[0] in ceva:
					URM.append(parte_dreapta[0])
	URM = list(set(URM)) # scoate duplicate values
	return URM

def genereaza_substitutii(sir):
	substitutii = []
	for regula in reguli_productie:
		if sir in regula[stanga]:
			substitutii.append(regula)
	return substitutii

def INC(INC):
	global reguli_productie
	copie_reguli_productie = reguli_productie[:]

	for regula_productie in INC:
		for regula in reguli_productie:
			sir = regula[stanga]
			dupa_punct = regula_productie[dreapta].split('.')[1]
			if dupa_punct != '':
				if dupa_punct[0].find(sir) != -1:
					substitutii = genereaza_substitutii(sir)
					for substitutie in substitutii:
						indice_regula = reguli_productie.index(substitutie)
						del reguli_productie[indice_regula]
						substitutie = (substitutie[stanga], '.' + substitutie[dreapta])
						INC.append(substitutie)
					break
		if reguli_productie == []:
			break

	reguli_productie = copie_reguli_productie[:]
	return INC

def SALT(I_n, caracter):
	I = []
	for regula in I_n:
		inainte_de_punct = regula[dreapta].split('.')[0]
		dupa_punct = regula[dreapta].split('.')[1]
		if dupa_punct == '':
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
reguli_productie = reguli_productie + [('S', start)]

reguli_cu_punct = []
for regula in reguli_productie:
	regula_cu_punct = (regula[stanga], '.' + regula[dreapta])
	reguli_cu_punct.append(regula_cu_punct)

C = []
I0 = INC([reguli_cu_punct[-1]])
C.append(I0)

F = []
for i in range (0,20):
	F.append(0)

for I_n in C:
	index = C.index(I_n)
	F[index] = dict.fromkeys(neterminale+terminale, -1)
	for caracter in neterminale + terminale:
		I = SALT(I_n, caracter)
		print("SALT(I" + str(C.index(I_n)) + ", '" + caracter + "')", end='')
		if I != []:
			if I not in C:
				C.append(I)
				index = C.index(I_n)
				F[index][caracter]=C.index(I)
				print('DA... ===> I' + str(C.index(I)))
			else:
				F[index][caracter]=C.index(I)
				print('NU...')
		else:
			print('NU...')

copie_reguli_productie =  reguli_productie[:]
reguli_productie[0] = (reguli_productie[0][stanga]+'$',reguli_productie[0][dreapta])
URM = dict.fromkeys(neterminale, [])
for caracter in neterminale:
	URM[caracter] = urm(caracter)
reguli_productie = copie_reguli_productie[:]

latime = len(terminale+neterminale)+1 # (+1 fiindca adaug si $)
inaltime = len(C)
# Tabel = [[0 for x in range(latime)] for y in range(inaltime)]
Tabel = []
for i in range (0,latime+1):
	Tabel.append(dict.fromkeys(terminale + ['$'] + neterminale))
# reguli_productie.append(('S',start))
reguli_productie = [('S',start)] + reguli_productie

for i in range (0, inaltime):
	I = C[i][:]
	while I != []:
		for regula in I:
			del I[I.index(regula)]
			parte_dreapta = regula[dreapta].split('.',1)[1]

			if parte_dreapta =='':
				if regula[dreapta].replace('.','') == start:
					Tabel[i]['$'] = 'acc'
				else:
					urm = URM[regula[stanga]]
					regula_fara_punct = (regula[stanga],regula[dreapta].replace('.',''))
					index = reguli_productie.index(regula_fara_punct)
					for x in urm:
						Tabel[i][x] = 'r' + str(index)

			else:
				caracter = parte_dreapta[0]
				if caracter in neterminale:
					ce_bag_in_tabel = F[i][caracter]
					Tabel[i][caracter] = ce_bag_in_tabel
				if caracter in terminale:
					ce_bag_in_tabel = F[i][caracter]
					Tabel[i][caracter] = 'd' + str(ce_bag_in_tabel)

# -----------------------------AFISARI----------------------------------

# i = 0
# for INC in C:
# 	print("I" + str(i))
# 	i += 1
# 	for regula in INC:
# 		print(regula[stanga] + " -> " + regula[dreapta])
#
# width = 4
# print('     |  ', end='')
# for caracter in neterminale + terminale:
# 	print(caracter.center(width), end='')
# print()
# print('---------------------------------------')
# for i in range (0, len(C)):
# 	print(str(i).center(width), end='')
# 	print("|".center(width), end='')
# 	for caracter in neterminale + terminale:
# 		if F[i][caracter] == -1:
# 			print('-'.center(width), end='')
# 		else:
# 			print(str(F[i][caracter]).center(width), end='')
# 	print()







