# Aluguel de carro

from math import ceil
from time import sleep

dias_alugados = str(input('\033[33mQuantos dias foram alugados?\033[m')).strip().split() # Pedir dias
print('-=' * 25)
print('\033[31m(Caso tenha usado metade de um dia, o valor será arredondado!)\033[m') # Informação, arredondar
print('-=' * 25)
sleep(1.5)
km_rodados = str(input('\033[33mQuantos quilômetros foram rodados?\033[m')).strip().split() # Pedir Km

dias_alugados = float(dias_alugados[0])
km_rodados = float(km_rodados[0])

dias_alugados = ceil(dias_alugados) # arredonda os dias
preco_aluguel = (dias_alugados * 60) + (km_rodados * 0.15)

print('-=' * 25)
print(f'Rodando \033[32m{dias_alugados}\033[m dias \033[31m(PODE ESTAR ARREDONDADO)\033[m e \033[32m{km_rodados}\033[m quilômetros.')
print(f'Seu aluguel ficou com o preço de \033[33mR${preco_aluguel}\033[m.')
print('-=' * 25)
print('__FIM__')