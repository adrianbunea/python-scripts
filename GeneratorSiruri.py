import string
import random

Neterminale = {'E','T','F'}
Terminale = {'a','+','*','(',')'}
Start = 'S'
P = [('E','E+T'),('E','T'),('T','T*F'),('T','F'),('F','a'),('F','(E)')]

# sir = Start
# while len(sir) < 60:
#     for caracter in sir:
#         if caracter in Neterminale:
            
Caracter = P[0][0]
print(Caracter)