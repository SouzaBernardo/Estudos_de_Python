# número inteiro e se é primo

def main():

    num = int(input('informe um número:'))
    total = 0

    print('Os número em azul são os que o seu número pode ser dividido:')

    for i in range(1, num+1):
        if num % i == 0:
            print('\033[34m', end=' ')
            total += 1
        else:
            print('\033[31m', end=' ')
        print(f'{i}', end=' ')

    print(f'\n\033[mO {num} foi dividido {total} vezes. Logo', end=', ')

    if total == 2:
        print('ele é primo.')
    else:
        print('não é primo.')


if __name__ == "__main__":
    main()
