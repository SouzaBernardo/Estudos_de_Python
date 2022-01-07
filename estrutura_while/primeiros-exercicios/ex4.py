'''
pede um número e mostra o fatorial, exemplo: 5! = 5x4x3x2x1 = 120 (while e for)
'''
# from math import factorial


def main():
    print('Calcular o fatorial:')
    num = int(input('Número: '))
    cont = num  # irá diminuir do número até 1
    f = 1  # fator nulo da multiplicação

    print(f'{num}! => ', end=' ')

    # com while
    while cont > 0:
        print(f'{cont}', end='')
        # implementação if-else dentro do print
        print(' x ' if cont > 1 else ' = ', end=' ')
        f *= cont
        cont -= 1
    print(f)

    '''
    ## outras formas de fazer:
    
    # com a lib
    f = factorial(num)

    # com for
    for i in range(1, cont):
        print(f'{cont}', end='')
        print(' x ' if cont > 1 else ' = ', end=' ')
        f *= cont
        cont -= 1
    '''


if __name__ == "__main__":
    main()
