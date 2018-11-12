import csv
stanga, dreapta = 0, 1

def citeste_tabel(nume_fisier):
    with open(nume_fisier, encoding='utf-8-sig') as fisier:
        reader = csv.DictReader(fisier)
        tabel = [linie for linie in reader]
    return tabel

def citeste_fisier(nume_fisier):
    gramatica = open(nume_fisier, 'r').read().replace('\n', '')

    neterminale = gramatica[gramatica.find("NETERMINALE:"): gramatica.find("TERMINALE:", gramatica.find("NETERMINALE:")+len("NETERMINALE:"))]
    gramatica = gramatica.replace(gramatica[gramatica.find("NETERMINALE:"): gramatica.find("TERMINALE:", gramatica.find("NETERMINALE:")+len("NETERMINALE:"))], '')
    neterminale = neterminale.replace("NETERMINALE:", '')
    neterminale = neterminale.split(' ')

    terminale = gramatica[gramatica.find("TERMINALE:") : gramatica.find("START:", gramatica.find("TERMINALE:")+len("TERMINALE:"))]
    gramatica = gramatica.replace(gramatica[gramatica.find("TERMINALE:") : gramatica.find("START:", gramatica.find("TERMINALE:")+len("TERMINALE:"))], '')
    terminale = terminale.replace("TERMINALE:", '')
    terminale = terminale.split(' ')

    start = gramatica[gramatica.find("START:") : gramatica.find("REGULI_PRODUCTIE:", gramatica.find("START:")+len("START:"))]
    start = start.replace("START:", '')

    reguli_productie = []
    reguli_productie_temp = gramatica[gramatica.find("REGULI_PRODUCTIE:"):]
    reguli_productie_temp = reguli_productie_temp.replace("REGULI_PRODUCTIE:", '')
    reguli_productie_temp = reguli_productie_temp.split(';')
    for regula in reguli_productie_temp:
        termen_stanga = regula.split('->')[stanga].replace(' ','')
        termeni_dreapta = regula.split('->')[dreapta].replace(' ', '').split('|')
        for termen in termeni_dreapta:
            reguli_productie.append((termen_stanga, termen))

    gramatica = {"neterminale" : neterminale, "terminale" : terminale, "start" : start, "reguli_productie" : reguli_productie}
    return gramatica
    
def sterge_lambda(sir):
    sir = sir.replace('_', '')
    return sir

def transforma_in_lista(sir, termeni):
    lista = []
    index = len(sir)-1
    substitutie = True
    while substitutie is True:
        substitutie = False
        index = len(sir)-1
        for termen in termeni:
            if sir.find(termen) >= 0 and sir.find(termen) < index:
                index = sir.find(termen)
                caractere = termen
        if index < len(sir)-1:
            substitutie = True
            sir = sir.replace(caractere,'',1)
            lista.append(caractere)
    lista.append(sir)
    return lista