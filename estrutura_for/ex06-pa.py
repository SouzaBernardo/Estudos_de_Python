# Progreção aritmética
'''
- primeiro termo e a razao de uma pa 10 primeiro termos
    -  inicial
    - diminuir o segundo com o primeiro
'''

def main():
    linha = '-=' * 16
    print(linha)
    term = int(input('Digite o primeiro termo da PA:'))
    r = int(input('Digite a razão da PA:'))
    print(linha)
    print('Os 10 primeiros temos da PA são:')

    for i in range(0, 10):
        print(term, end=' ')
        term += r

    print(f'\n{linha}')        

if __name__ == "__main__":
    main()