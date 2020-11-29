from random import randint
numero = randint(1, 100)
print('Sorteando um número...')
print('O número sorteado é {}.'.format(numero))
if numero % 2 == 0:
    print('Este número é par!')
else:
    print('Este número é impar!')
print('_FIM_')
