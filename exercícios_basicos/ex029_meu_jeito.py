from random import randint
# Criar aleatórios
a = randint(0, 100)
b = randint(0, 100) - a
c = randint(0, 100) - b
# Mostrar sorteados
print(a, b, c)
# Escolhendo o maior
if b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c
else:
    maior = a
# Escolhendo o menor
if b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c
else:
    menor = a
# Resultado
print('-=-' * 10)
print('A ordem crescente é {} e {}.'.format(menor, maior))
print('A ordem decrescente é {} e {}'.format(maior, menor))
print('-=-' * 10)
print('O maior é {}'.format(maior))
print('O menor é {}'.format(menor))
