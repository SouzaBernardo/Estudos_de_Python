'''
    DIZER SE É UM  palindromo -> de tras pra frente
        - desconsiderar os espaços e os acentos
'''
# Revisado ...
def main():
    linha = '-=' * 16
    print(linha)
    frase = input('Digite a palavra escolhida:').strip().upper()
    palavras = frase.split()
    junto = ''.join(palavras)
    inverso = ''
    #inverso = junto[::-1] => mas ai não da para usar o for...
    for letra in range(len(junto) - 1, -1, -1): 
        inverso += junto[letra]
    '''    
        #len(junto) - 1 => do 0 ao 19, por exemplo...
        # -1 => O segundo -1 é para ele começar do final, posição -1
        # -1 => O último -1 é para ele ir voltando uma letra 
    '''
    print(linha)
    print(f'O inverso de {junto} é: \033[32m{inverso}\033[m.')
    print(linha)
    if inverso == junto:
        print('É um palindromo!')
    else:
        print('Não é um palindromo...')
    print(linha)
if __name__ == "__main__":
    main()