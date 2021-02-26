# Numeros pares entre 1 e 50
from math import ceil, floor
x = int(input('Digite um número:'))
y = int(x / 2)
if y % 2 != 0:
    y = floor(y)  # analizar aqui
for intervalo in range(1, y):
    if x % 2 == 0:
        x -= 2
    else:
        x -= 1  # números impares não entregam o dois
    print(x)
print(y)
