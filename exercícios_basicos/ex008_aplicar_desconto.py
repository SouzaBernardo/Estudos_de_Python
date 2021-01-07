# CALCULAR DESCONTO DO PRODUTO
preco = float(input('\033[33mQual o preço do produto? R$'))
desconto = str(input('E o desconto que será aplicado?\033[m')).upper().strip() # desconto
# Caso o desconto tenha % ou porcento, ignorar
if desconto.count('PORCENTO'):
    desconto = desconto.replace('PORCENTO', '')
elif desconto.count('%'):
    desconto = desconto.replace('%', '')
desconto = float(desconto)
aplicar_desconto = preco * desconto / 100
print('\033[32m-=' * 9 + '\033[m')
print(f'Seu produto de \033[33mR${preco:.2f}\033[m com desconto de \033[33m{desconto:.2f}%\033[m.')
print(f'Ficou \033[33mR${aplicar_desconto:.2f}\033[m.')
print('\033[32m-=' * 9 + '\033[m')
