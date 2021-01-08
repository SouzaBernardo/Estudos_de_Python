# Aluguel de carro
from math import ceil

dias_alugados = str(input('Quantos dias foram alugados?')).lower().strip() # Pedir dias

print('(Caso tenha usado metade de um dia, o valor será arredondado!)') # Informação, arredondar

km_rodados = str(input('Quantos quilômetros foram rodados?')).lower().strip() # Pedir Km

dias_alugados = float(dias_alugados.split()[0])
km_rodados = float(km_rodados.split()[0])

dias_alugados = ceil(dias_alugados) # aqui arredonda os dias
preco_aluguel = (dias_alugados * 60) + (km_rodados * 0.15)

print(f'Rodando {dias_alugados} dias (PODE ESTAR ARREDONDADO) e {km_rodados} quilômetros.')
print(f'Seu aluguel ficou com o preço de R${preco_aluguel}.')