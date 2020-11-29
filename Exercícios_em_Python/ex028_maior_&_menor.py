print('Quero que você me de 3 números')
n1 = input('Primeiro:')
n2 = input('Segundo:')
n3 = input('Terceiro:')
menor = n1
maior = n1
meio = n1

# Analisar quem é menor
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# Analisar quem é maior
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3

# Analisar o do meio
if n2 > menor and n2 < maior:
    meio = n2
if n3 > menor and n3 < maior:
    meio = n3

print('O menor é {}.'.format(menor))
print('o número mediano é {}'.format(meio))
print('O maior é {}'.format(maior))
print('A ordem crescente é {}, {}, {}'.format(menor, meio, maior))
print('_FIM_')
