# Numeros pares entre 1 e 50
from math import ceil, floor
x = int(input('Digite um número:'))
y = int(x / 2)
if y % 2 != 0:
    y = floor(y + 1)
for intervalo in range(1, y):
    if x % 2 == 0:
        x -= 2
    else:
        x -= 1
    print(x)
print(y)
