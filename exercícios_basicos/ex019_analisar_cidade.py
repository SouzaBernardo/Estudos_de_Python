# Analisar o nome da cidade
nome = str(input('Digite o nome da sua cidade:')).upper().strip()
if nome.count('SANTO'):
    vezes_que_aparece = nome.count('SANTO')
    print('Sua cidade tem em seu nome a palavra "SANTO"!') 
    print(f'Essa palavra aparece {vezes_que_aparece} vezes.')
else:
    print('Sua cidade não contém a palavra "SANTO"!')
