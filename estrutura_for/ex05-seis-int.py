# 6 numeros int mostrar somas dos pares

def main():
    pair = 0
    for i in range(0, 7):
        num = int(input('Enter a number:'))
        if (num % 2 == 0):
            pair += num
    print(f'The sum of all pair numbers is: {pair}')

if __name__ == "__main__":
    main()