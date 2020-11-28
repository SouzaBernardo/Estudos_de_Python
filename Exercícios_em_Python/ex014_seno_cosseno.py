# Pedir o angulo e dizer qual é o seno, conseno e tangente
from math import radians, sin, cos, tan

# Pedi o angulo
angulo = float(input('Angulo que você deseja:'))

# Cacular os resultados
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

# Dar os resultados
print(f'O seno é {seno}.')
print(f'O cosseno é {cosseno}.')
print(f'A tangente é {tangente}.')

# Fim do programa
print('__FIM__')