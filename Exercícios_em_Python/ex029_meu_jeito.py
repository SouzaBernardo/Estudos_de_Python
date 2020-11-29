from random import randint

a = randint(0, 100)
b = randint(0, 100) - a
c = randint(0, 100) - (a and b)

maior = a
medio = a
menor = a

print(a, b, c)

# Escolhendo o maior
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
# Escolhendo o menor
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

print('A ordem crescente é {}, {} e {}.'.format(menor, medio, maior))
print('A ordem decrescente é {}, {} e {}'.format(maior, medio, menor))
print('O maior é {}'.format(maior))
print('O menor é {}'.format(menor))
