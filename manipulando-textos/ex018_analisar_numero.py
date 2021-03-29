'''
from random import randint

# num = randint(0, 9999)
# linha tirada para 
'''
num = int(input('Número inteiro:'))
# divide e pega o resto
unidade = num // 1 % 10 
# se 10 for 100 => pega 2 digitos
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print('análisando...')
print(f'O número é \033[31m{num}\033[31m')
print(f'Unidade: \033[31m{unidade}\033[m')
print(f'Dezena: \033[31m{dezena}\033[m')
print(f'Centena: \033[31m{centena}\033[m')
print(f'Milhar: \033[31m{milhar}\033[m')
'''
n=str(num)
print('análisando...')
print(f'O número é \033[31m{n[-1]}\033[31m')
print(f'Unidade: \033[31m{n[-2]}\033[m')
print(f'Dezena: \033[31m{n[-3]}\033[m')
print(f'Centena: \033[31m{n[-4]}\033[m')
print(f'Milhar: \033[31m{n[0]}\033[m')
'''