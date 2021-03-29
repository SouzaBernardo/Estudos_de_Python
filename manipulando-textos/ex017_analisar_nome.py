# Pedir o nome da pessoa, e analisa-lo
nome = str(input('\033[33mQual será o nome para analisar?\033[m')).strip()

#maiusculo = nome.upper()
#minusculo = nome.lower()
quantidade_de_letras = len(nome) - nome.count(' ')
quantidade_letra_primeiro = len(nome.split()[0])

print(f'Nome em MAIÚSCULO: \033[33m{nome.upper()}\033[m.')
print(f'Nome minúsculo: \033[33m{nome.lower()}\033[m.')
print(f'O nome tem \033[33m{quantidade_de_letras}\033[m letras.')
print(f'O primeiro nome tem \033[33m{quantidade_letra_primeiro}\033[m letras')
print('__FIM__')