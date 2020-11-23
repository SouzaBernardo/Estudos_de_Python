# Realizar a média anual de um aluno...

print('Olá, vamos descobrir a sua média no ano?') # Dar olá para pessoa

# Atribuir valor dos semestres para as variáveis
nota_primeiro = float(input('Qual a sua nota TOTAL do primeiro semestre?')) # Pedir o primeiro valor, a nota do 1° semestre
nota_segundo = float(input('E a do segundo semestre? Qual a sua nota?')) # pedir o segundo valor, a nota do 2° semestre
media_resposta = (nota_primeiro + nota_segundo) / 2

# Dizer ao user qual é as notas e a sua média...
print('Sua nota do primeiro semestre foi {:.1f}'.format(nota_primeiro))
print('E, sua nota do segundo semestre foi {:.1f}'.format(nota_segundo))
print('Portanto, sua media deste ano foi {:.1f}.'.format(media_resposta))

# __FIM__
print('__FIM__')