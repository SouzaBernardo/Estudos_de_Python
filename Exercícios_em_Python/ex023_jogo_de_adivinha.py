# Jogo de Adivinha
from random import randint 
from colorama import init
init()

# Número entre 0 e 5
num = randint(0, 5)

# Dar o desafio
print('Escolhi um número de 0 à 5.')
pergunta = int(input(('Sabe qual é?')))

# Condições
if pergunta == num:
    print('\033[32mAcertou!!!') # Se acertar o número
else:
    print('\033[31mErrou!!!\033[m Tente novamente...') # Se errar o número

# Resultado
print(f'O número era {num}')
print('__FIM__')
