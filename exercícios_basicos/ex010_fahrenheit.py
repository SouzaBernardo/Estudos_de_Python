# Transformar grau Celsius para Grau Fahrenheit
from time import sleep

grau_cel = str(input('\033[33mInforme a temperatura em Grau Celsius:\033[m')).strip()

lista = grau_cel.split()  # Cria um array com o número e seus complementos
so_numero = lista[0]  # Pega o primeiro valor, o número
so_numero = float(so_numero)

grau_fah = 9 * so_numero / 5 + 32  # calcula Fahrenheit
kelvin = so_numero + 273.15  # calcula Kelvin

print(f'A temperatura em \033[33mGrau Celsius\033[m é \033[33m{so_numero} °C\033[m.')
sleep(1)
print('\033[31mCONVERTENDO...\033[m')
sleep(1)

print('\033[31m-=' * 10 + '\033[m')
print(f'Temperatura convertida para \033[32mGrau Fahrenheit: {grau_fah}°F\033[m;')
print(f'Temperatura convertida para \033[32mKelvin: {kelvin}°K\033[m;')
print('\033[31m-=' * 10 + '\033[m')
print('__FIM__')
