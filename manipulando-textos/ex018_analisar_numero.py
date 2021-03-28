from random import randint

num = randint(0, 9999)
# linha tirada para 
#num = int(input('Número inteiro:'))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print('análisando...')
print(f'O número é \033[31m{num}\033[31m')
print(f'Unidade: \033[31m{unidade}\033[m')
print(f'Dezena: \033[31m{dezena}\033[m')
print(f'Centena: \033[31m{centena}\033[m')
print(f'Milhar: \033[31m{milhar}\033[m')
