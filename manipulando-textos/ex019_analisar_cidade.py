# Analisar o nome da cidade
nome = str(input('\033[33mDigite o nome da sua cidade:\033[m')).upper().strip()
if nome.count('SANTO'):
    vezes_que_aparece = nome.count('SANTO')
    print('\033[32mSua cidade tem em seu nome a palavra "SANTO"!\033[m') 
    print(f'Essa palavra \033[33maparece {vezes_que_aparece} vezes\033[m.')
else:
    print('\033[31mSua cidade não contém a palavra "SANTO"!\033[m')
