# Aluguel de carro

from math import ceil

dias_alugados = str(input('Quantos dias foram alugados?')).lower().strip() # Pedir dias
print('(Caso tenha usado metade de um dia, o valor será arredondado!)') # Informação, arredondar
km_rodados = str(input('Quantons quilômetros foram rodados?')).lower().strip() # Pedir Km

# Desconsiderar dados adicionais, considerar somente os números
if dias_alugados.count('dias') or dias_alugados.count('dia'):
    # Desconsiderar os dias/ dia
    dias_alugados = dias_alugados.replace('dias', '')
    dias_alugados = dias_alugados.replace('dia', '')
if km_rodados.count('quilômetros') or km_rodados.count('quilômetro'):
    # Desconsidera com acento
    km_rodados = km_rodados.replace('quilômetros', '')
    km_rodados = km_rodados.replace('quilômetro', '')
if km_rodados.count('quilometros') or km_rodados.count('quilometro'):
    # Desconsidera sem acento
    km_rodados = km_rodados.replace('quilometros', '')
    km_rodados = km_rodados.replace('quilometro', '')
if km_rodados.count('km/h') or km_rodados.count('km'):
    # Desconsiderar km/h ou km
    km_rodados = km_rodados.replace('km/h', '')
    km_rodados = km_rodados.replace('km', '')

# Converter de str para float
dias_alugados = float(dias_alugados)
km_rodados = float(km_rodados)

# Arredondar dias
dias_alugados = ceil(dias_alugados)

# Calcular o preço do aluguel
preco_aluguel = (dias_alugados * 60) + (km_rodados * 0.15)

# Resultado
print(f'Rodando {dias_alugados} dias (PODE ESTAR ARREDONDADO) e {km_rodados} quilômetros.')
print(f'Seu aluguel ficou com o preço de R${preco_aluguel}.')