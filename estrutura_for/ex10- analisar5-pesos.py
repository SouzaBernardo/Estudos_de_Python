'''
- ler peso de 5 pessoas e dizer qual o maior e o menor
'''
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'{p}° Peso:'))
    if p == 1:
        # já que antes do 1º não tem maior ou menor, o primeiro recebe os dois
        maior = peso
        menor = peso
    else:
        # Vai comparar com o primeiro, alterando o valor de maior ou menor
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O menor peso foi: {menor} Kg')
print(f'O maior peso foi: {maior} Kg')