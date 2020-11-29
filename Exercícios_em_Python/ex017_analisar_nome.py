# Pedir o nome da pessoa, e analisa-lo

# Pedir o nome
nome = str(input('Qual será o nome para analisar?')).strip()

# Analisar
maiusculo = nome.upper()
minusculo = nome.lower()
quantidade_de_letras = len(nome) - nome.count(' ')
quantidade_letra_primeiro = len(nome.split()[0])

# Resultado
print(f'Nome em MAIÚSCULO: {maiusculo}.')
print(f'Nome minúsculo: {minusculo}.')
print(f'O nome tem {quantidade_de_letras} letras.')
print(f'O primeiro nome tem {quantidade_letra_primeiro} letras')