from random import randint
num = randint(0, 5)
print('Escolhi um número de 0 à 5.')
pergunta = int(input(('Sabe qual é?')))
if pergunta == num:
    print('Acertou!!!')
else:
    print('Errou!!! Tente novamente...')
print('O número era {}'.format(num))