# DESCONTO DO PRODUTO -> calculador

valor = str(input('Qual o preço do produto?')).upper().strip() # Preço
desconto = str(input('E o desconto que será aplicado?')).upper().strip() # desconto

# Caso o valor tenha reais ou R$, ignorar

if valor.count('REAIS'):
    valor = valor.replace('REAIS', '') # Ignora REAIS
if valor.count('R$'):
    valor = valor.replace('R$', '') # Ignora R$

# Caso o desconto tenha % ou porcento, ignorar

if desconto.count('PORCENTO'):
    desconto = desconto.replace('PORCENTO', '') # ignora PORCENTO
if desconto.count('%'):
    desconto = desconto.replace('%', '')

# Transformar as variáveis de STR para FLOAT

valor = float(valor)
desconto = float(desconto)
aplicar_desconto = valor * desconto / 100 # aplicar o desconto


# Dizer o resultado do desconto

print(f'Seu produto de R${valor} com desconto de {desconto}%.')
print(f'Ficou R${aplicar_desconto}.')