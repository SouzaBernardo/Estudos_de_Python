# Dizer o aumento do salário
salario = float(input('\033[33mOlá, qual seu salário atual? R$'))
aumento = str(input('E qual a porcentagem para o aumento?')).upper().strip()
# Desconsiderar % e PORCENTO
if aumento.count('PORCENTO'):
    aumento = aumento.replace('PORCENTO', '')
elif aumento.count('%'):
    aumento = aumento.replace('%', '')
aumento = float(aumento)
aplicar_aumento = (salario * aumento / 100) + salario
print(f'\033[33mAntigamente\033[m seu salário \033[33mera R${salario:.2f}\033[m.')
print(f'E, você \033[33mrecebeu\033[m um aumento de \033[33m{aumento:.2f}%\033[m.')
print(f'O \033[32maumento do seu salário ficou {aplicar_aumento:.2f}\033[m.')
print('__FIM__')
