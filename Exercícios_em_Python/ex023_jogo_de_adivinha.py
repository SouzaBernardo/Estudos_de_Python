# Jogo de Adivinha
from random import randint 

# Número entre 0 e 5
num = randint(0, 5)

# Dar o desafio
print('Escolhi um número de 0 à 5.')
pergunta = int(input(('Sabe qual é?')))

# Condições
if pergunta == num:
    print('Acertou!!!') # Se acertar o número
else:
    print('Errou!!! Tente novamente...') # Se errar o número

# Resultado
print(f'O número era {num}')
print('__FIM__')
