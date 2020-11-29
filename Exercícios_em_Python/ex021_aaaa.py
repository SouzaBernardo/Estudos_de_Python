frase = str(input('Frase:')).upper().strip()
print('A frase contém {} letra(s) a / as. '.format(frase.count('A')))
print('Nessa frase, a primeira letra A se encontra na posição {}'.format(frase.find('A') + 1))# + 1 pq inicia em 0
print('Já a ultima é na posição {}.'.format(frase.rfind('A') + 1))# Há um problema de negação a palavras com acento
