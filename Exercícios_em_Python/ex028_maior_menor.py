# Descobrir qual número é maior, menor e o do meio
print('-=-' * 10)
print('Diga-me 3 números e vou dizer qual deles é maior, menor, medio e a ordem crescente!')
n1 = float(input('Primeiro:'))
print('-=-' * 10)
n2 = float(input('Segundo:'))
print('-=-' * 10)
n3 = float(input('Terceiro:'))
print('-=-' * 10)
# Analisar quem é menor, maior e mediana
if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3
else:
    menor = n1
# Analisar quem é maior
if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n2 and n3 > n1:
    maior = n3
else:
    maior = n1
# Analisar o do meio
if n2 > menor and n2 < maior:
    meio = n2
elif n3 > menor and n3 < maior:
    meio = n3
else:
    meio = n1
print(f'O menor é {menor}.')
print(f'o número mediano é {meio}')
print(f'O maior é {maior}')
print(f'A ordem crescente é {menor}, {meio}, {maior}')
print('_FIM_')
