# Dizer a categoria de um atleta
print('Vamos descobrir qual é sua categoria!')
# Pedir idade
idade_str = input('Qual a sua idade?').strip().lower() # Deixar minúsculo e separa as palavras
# Converter str para int
idade_int = int(idade_str.split()[0])
# Verificar a categoria do jovem
if idade_int <= 9:
    print('Sua categoria é MIRIM!') # Para menores de 9 anos
elif idade_int <= 14:
    print('Sua categoria é INFATIL') # Para menores de 14 anos
elif idade_int <= 19:
    print('Sua categoria é JÚNIOR') # Para menores de 19 anos
elif idade_int <= 20:
    print('Sua categoria é SÊNIOR') # Para menores de 20 anos
else:
    print('Sua categoria é MASTER') # Para maiores de 20 anos
# Indicar a idade recebida
print(f'Devido a sua idade que é {idade_int} anos.')
print('__FIM__') # Fim do programa