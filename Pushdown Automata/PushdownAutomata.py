from Functii import citeste_tabel, stanga, dreapta, citeste_fisier, transforma_in_lista
import argparse
import csv

def actiune(indice, termen):
    global sir, stiva, tabel
    valoare = list(tabel[int(indice)][termen])
    if(valoare[0] == 'd'):
        deplasare(''.join(valoare[1:]))
    elif(valoare[0] == 'r'):
        reducere(''.join(valoare[1:]))
    elif(valoare == list('ac')):
        return True
    else:
        print("Actiune nerecunoscuta!")
        return False
    return False

def deplasare(stare):
    stiva.append(sir[0])
    stiva.append(stare)
    sir.remove(sir[0])

def reducere(numar_productie):
    global reguli_productie
    regula = reguli_productie[int(numar_productie)-1]
    while stiva[-1] != regula[dreapta][0]:
        stiva.pop()
    stiva.pop()
    stiva.append(regula[stanga])

def salt(indice, termen):
    global sir, stiva, tabel
    valoare = tabel[int(indice)][termen]
    stiva.append(valoare)

parser = argparse.ArgumentParser()
# parser.add_argument("nume_gramatica", help = "alege un fisier text din care sa fie citita gramatica")
parser.add_argument("nume_tabel", help = "alege un fisier text din care sa fie citit tabelul")
parser.add_argument("sir_intrare", help = "introdu un sir de intrare")
args = parser.parse_args()

# gramatica = citeste_fisier(args.nume_gramatica)
neterminale = ['E','T','F']
terminale = ['a','+','-','*','/','(',')']
reguli_productie = [('E','E+T'),
                    ('E','T'),
                    ('T','T*F'),
                    ('T','F'),
                    ('F','(E)'),
                    ('F','a'),
                    ('F','-(E)')]

tabel = citeste_tabel(args.nume_tabel)
print(tabel[0].keys())
for linie in tabel:
    for key in linie:
        if linie.get(key) == '':
            linie[key] = '--'
    print(linie.values())

stiva = ['$','0']
sir_intrare = args.sir_intrare + '$'   
sir = transforma_in_lista(sir_intrare, neterminale+terminale)
print(sir)

acceptat = False
while acceptat is False:
    termen = stiva[-1]  # Ia ultimul element din stiva
    if termen.isdigit() is True:
        indice = termen
        termen = sir[0]
        acceptat = actiune(indice, termen)
        print("STIVA: \"" + ''.join(stiva) + "\" | SIR: \"" + ''.join(sir) + "\"")
    else:
        indice = stiva[-2]
        termen = stiva[-1]
        salt(indice,termen)
        print("STIVA: \"" + ''.join(stiva) + "\" | SIR: \"" + ''.join(sir) + "\"")
print("SIR ACCEPTAT!")