# Pedir o angulo e dizer qual é o seno, conseno e tangente
from math import radians, sin, cos, tan
an = float(input('angulo que você deseja:'))
seno = sin(radians(an))
print('O seno é {}.'.format(seno))
cosseno = cos(radians(an))
print('O cosseno é {}.'.format(cosseno))
tangente = tan(radians(an))
print('A tangente é {}.'.format(tangente))
