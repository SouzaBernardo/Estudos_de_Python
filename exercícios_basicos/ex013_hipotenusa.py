# Calculadora de hipotenusa

from math import hypot

cateto_ad = float(input('\033[33mCateto adjacente:\033[m'))
cateto_op = float(input('\033[33mCateto oposto:\033[m'))
hipo = hypot(cateto_ad, cateto_op) # Calcular a hipotenusa

print('-=' * 45)
print(f'\033[mA \033[33mhipotenusa\033[m, do cateto oposto de valor {cateto_op} e cateto adjacente de valor {cateto_ad}, é: \033[33m{hipo :.2f}\033[m.')
print('-=' * 45)

print('\033[31m__FIM__\033[m')
