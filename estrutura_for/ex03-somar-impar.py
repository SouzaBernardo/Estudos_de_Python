# soma de numero impar que são multiplos de 3 entre 1 e 500
x = int(input('Número inteiro:'))
y = x + 1
impar = 1
for multiplos in range(1, y):
    if x % 2 != 0:
        print(x)
    x -= 1
