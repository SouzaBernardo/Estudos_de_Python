from time import sleep
from sys import stdout


def barra(v):
    v = int(v)
    print('[ ', end='')
    for v in range(0, v):
        print(f'-', end='', flush=True)
        sleep(0.1)
    print(' ]', end='\n')


def calcularNotas():
    soma = 0
    v = 0
    for i in range(0, 2):
        nota = float(input(f'\n{i + 1}º nota : '))
        soma += nota
    v = soma // 2
    print('\nCALCULANDO:  ', end='\b')
    barra(v)
    return print(f'MÉDIA FOI: {soma / 2}')


def main():
    calcularNotas()
    sleep(1)
    print('\n__FIM__\n')


if __name__ == "__main__":
    main()
