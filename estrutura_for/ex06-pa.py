# Progreção aritmética
'''

- primeiro termo e a razao de uma pa 10 primeiro termos


-  inicial

- diminuir o segundo com o primeiro
'''

def main():
    print('Enter the first 10 terms')

    terms = []# all terms
    cont = 1 # st
    ant = 0 #anterior
    term = 0 # the term
    r = 0 #reason
    
    for i in range(0, 10):
        ant = term
        term = int(input(f'Enter {cont}st the here:'))
        cont += 1 # number st
        r =  term - ant # ap
        terms.append(term)
    # finish tomorrow---------
    print(f'The terms are {terms}')
    print(f'The reason is {r}') # this

if __name__ == "__main__":
    main()