'''
ler o primeiro termo e a razão da pa, e mostrar os 10 primeiros termos
'''


def main():
    print('|********PROGRESSÃO ARITMÉTICA********|')
    termo = int(input('-> Primeiro termo da PA: '))
    razao = int(input('-> Razão da PA: '))
    total = 0
    cont = 10
    while cont > 0:
        print(f'{termo}', end='')
        print(' + ' if cont > 1 else ' = ', end='')
        termo += razao
        total += termo
        cont -= 1
    print(f'{total}')


if __name__ == "__main__":
    main()
