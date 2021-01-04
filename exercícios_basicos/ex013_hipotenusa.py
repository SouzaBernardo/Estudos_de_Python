# Calculadora de hipotenusa
from math import hypot

# Pedir os catetos
cateto_ad = float(input('Cateto adjacente:')) # Cateto Adjacente
cateto_op = float(input('Cateto oposto:')) # Cateto oposto
hipo = hypot(cateto_ad, cateto_op) # Calcular a hipotenusa

# Resultado
print(f'A hipotenusa, do cateto oposto de valor {cateto_op} e cateto adjacente de valor {cateto_ad}, é: {hipo :.2f}')
print('__FIM__')
