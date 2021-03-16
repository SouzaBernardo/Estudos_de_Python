# Tabuada

def tabuada(num, mul):
    for m in range(0, 11):
        print('=' * 13)
        print(f'{num} X {mul} = {num*mul}')
        mul += 1
    print('='*13)


def main():
    print('=' * 13)
    print('Vamos ver a tabuada!')
    print('=' * 13)
    mul = 0
    num = int(input('Qual o número que você quer saber a tabuada? (número inteiro!)'))

    tabuada(num, mul)

if __name__ == "__main__":
    main()