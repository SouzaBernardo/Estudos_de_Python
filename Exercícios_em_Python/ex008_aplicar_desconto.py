# Dizer o desconto do produto
valor = str(input('Qual o preço do produto?')).upper().strip() # Preço
desconto = str(input('E o desconto que será aplicado?')).upper().strip() # desconto
# Caso o valor tenha reais ou R$, ignorar
if valor.count('REAIS'):
    valor = valor.replace('REAIS', '') # Substitui REAIS para ''
if valor.count('R$'):
    valor = valor.replace('R$', '') # Substitui R$ para ''
# Calcula o desconto
valor = float(valor)
#aplicar_desconto = valor * desconto / 100
print(valor)