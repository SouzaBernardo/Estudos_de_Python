# soma de numero impar que são multiplos de 3 entre 1 e 500

soma_impar = 0

for multiplos in range(1, 501):
    if multiplos % 3 == 0:
        soma_impar += multiplos
        print(soma_impar)
