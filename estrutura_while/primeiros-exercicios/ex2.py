from random import randint

'''
pensar um número e dizer quando o usuário acertou, e dizer a quantidade de palpites dados
'''


def main():
    # variáveis
    num = randint(1, 10)
    num_user = 0
    palpites = 0
    flag = True

    # inicio para o usuário
    print('E ai, eu escolhi um número de 1 a 10, consegue adivinha-lo?')

    while flag == True:
        num_user = int(input('Seu palpite: '))
        if num_user == num:
            flag = False
        else:
            palpites += 1

    print(
        f'Parabéns!!! Você acertou com {palpites} tentativas, o número era {num}.')


if __name__ == '__main__':
    main()
