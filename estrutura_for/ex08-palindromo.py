'''
    DIZER SE É UM  palindromo -> de tras pra frente
        - desconsiderar os espaços e os acentos
'''

def main():
    palavra = input('Digite a palavra escolhida:')
    lista = list(palavra)
    #como inverter uma lista ?
    #inverso_lista = reversed(lista)
    if lista == 0:
        print('É um palindromo!')
    else:
        print('Não é um palindromo!')
    print(lista, palavra)

if __name__ == "__main__":
    main()