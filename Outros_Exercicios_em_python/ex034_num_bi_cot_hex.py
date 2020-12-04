# Escolher um número e se que ele em Binário, Octal ou Hexadecimal
print('Olá! Escolha um número inteiro e vamos converter suas bases.')
# Pedir o número
numero_escolhido = int(input('Digite o número:'))
# Dar opções
print('Escolha a base que você quer converter...')
print('[1] - Binário')
print('[2] - Octal')
print('[3] - Hexadecimal')
# Pedir escolha
escolha_da_base = int(input('Qual base que deseja?'))
# Converter para as bases
if escolha_da_base == 1:
    numero_escolhido_convertido = bin(numero_escolhido)
    print('ANALISANDO...')
    print('Convertemos seu número para BINÁRIO!')
    print(f'Seu número ({numero_escolhido}) em binário é {numero_escolhido_convertido}.')
