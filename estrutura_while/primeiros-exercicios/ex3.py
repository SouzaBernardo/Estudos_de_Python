'''
ler dois valores
    MENU:
        1- soma,
        2- multplicar,
        3- maior,
        4- novos números,
        5- sair
'''


def main():
    linha = '-=' * 18  # charme

    print(linha)

    # valores
    num1 = int(input('Digite o primeiro valor inteiro: '))
    num2 = int(input('Digite o segundo valor inteiro: '))
    resposta = -1

    print(linha)

    while resposta != 5:
        if resposta != 5:
            resposta = menu()  # guarda a resposta do usuário na variavel resposta
        print('\n' + linha)

        # alternativas
        if resposta == 1:
            print(f'Soma: {num1} + {num2} = {num1 + num2}')
        elif resposta == 2:
            print(f'Multiplicação: {num1} x {num2} = {num1 * num2}')
        elif resposta == 3:
            if num1 > num2:
                print(f'O maior valor é {num1}')
            else:
                print(f'O maior valor é {num2}')
        elif resposta == 4:
            print('Novos valores:')
            # talvez aqui tenha algum problema de pilha, mas ainda não tenho certeza...
            main()
        elif resposta == 5:
            print('Finalizando o programa...')
            break

        print(linha)
    print(linha)


def menu():
    print('\nOperações (digite o número da operação abaixo para realiza-la):')
    print('1- Somar\n2- Multiplicar\n3- Verificar o maior\n4- Novos números\n5- Sair')
    operacao = int(input('Qual operação deseja fazer? '))
    return operacao


if __name__ == "__main__":
    main()
