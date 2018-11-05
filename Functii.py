stanga, dreapta = 0, 1

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