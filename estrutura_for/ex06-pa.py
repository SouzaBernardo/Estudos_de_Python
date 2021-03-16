# Progreção aritmética
'''

- primeiro termo e a razao de uma pa 10 primeiro termos


-  inicial

- diminuir o segundo com o primeiro
'''

def main():
    # estavs errado 
    term = int(input('Digite o primeiro termo da PA:'))
    r = int(input('Digite a razão da PA:'))

    for i in range(0, 10):
        print(term)
        term += r
        

if __name__ == "__main__":
    main()