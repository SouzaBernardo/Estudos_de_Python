'''
- ler peso de 5 pessoas e dizer quel qual o maior e o menor
'''
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'{p}° Peso:'))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O menor peso foi: {menor} Kg')
print(f'O maior peso foi: {maior} Kg')