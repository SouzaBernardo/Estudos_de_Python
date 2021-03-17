'''
    DIZER SE É UM  palindromo -> de tras pra frente
        - desconsiderar os espaços e os acentos
'''
# antes da revisão ...
def main():
    palavra = input('Digite a palavra escolhida:').upper()
    lista = list(palavra)
    #como inverter uma lista ?
    inverso_lista = lista[::-1] # assim podemos inverter uma lista...
    if lista == inverso_lista:
        print('É um palindromo!')
    else:
        print('Não é um palindromo!')

if __name__ == "__main__":
    main()