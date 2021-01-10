# Pedir o angulo e dizer qual é o seno, conseno e tangente
from math import radians, sin, cos, tan

angulo = float(input('\033[33mAngulo que você deseja:\033[m'))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('-=' * 8)
print(f'O \033[32mseno\033[m: \033[34m{seno:.2f}\033[m.')
print(f'O \033[32mcosseno\033[m: \033[34m{cosseno:.2f}\033[m.')
print(f'A \033[32mtangente\033[m: \033[34m{tangente:.2f}\033[m.')
print('-=' * 8)
print('__FIM__')