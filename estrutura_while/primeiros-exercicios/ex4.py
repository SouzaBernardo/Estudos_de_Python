'''
pede um número e mostra o fatorial, exemplo: 5! = 5x4x3x2x1 = 120 (while e for)
'''
# from math import factorial


def main():
    print('Verificar o fatorial:')
    num = int(input('Número: '))
    cont = num
    f = 1

    # com a lib
    # f = factorial(num)

    # com while
    while cont > 0:
        print(f'{cont}')
        f *= cont
        cont -= 1

    # com for
    '''
    for i in range(1, cont):
        print(f'{cont}',)
        f *= cont
        cont -= 1
    '''
    # resposta
    print(f'{num}! = {f}')


if __name__ == "__main__":
    main()
