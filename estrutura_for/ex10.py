'''
- ler peso de 5 pessoas e dizer quel qual o maior e o menor
'''
'''
peso = 0 => desnecessário
peso_anterior = 0 => desnecessário
contador = 1 => desnecessário
maior = 0
menor = 0
for i in range(0, 5):

    peso_anterior = peso => não precisava
    peso = float(input(f'{contador}° Peso:'))
    contador += 1 => desnecessário
    
    if peso > peso_anterior:
        maior = peso
        menor = peso_anterior
    else:
        maior = peso_anterior
        menor = peso

    print(f'peso: {peso}\npeso anterior: {peso_anterior}\npeso maior: {maior}\npeso menor: {menor}')
    if peso < peso_anterior:
        menor = peso
    else:
        menor = peso_anterior
'''
# =========================================
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