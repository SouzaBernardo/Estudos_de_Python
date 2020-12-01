# Sortear número e dizer se é par ou impar
from random import randint

# Sortea o número
numero = randint(1, 100)

# Informa número sorteado
print('Sorteando um número...')
print('O número sorteado é {}.'.format(numero))

# Identificar se é ou não par
if numero % 2 == 0:
    print('Este número é par!') # Para PAR
else:
    print('Este número é impar!') # Para IMPAR
# FIM
print('_FIM_')
