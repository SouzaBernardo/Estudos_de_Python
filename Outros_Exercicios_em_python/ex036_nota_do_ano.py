# Dizer a média anual de um aluno e dizer se ele passou.
print('BOLETIM:') # inicio
print('Para saber se você passou, preciso das suas notas do 1° e 2° semestre...')
# Perguntar as notas
pri_sem = float(input('Primeiro semestre:'))
seg_sem = float(input('Segundo semestre:'))
# Calcula a média
med_ano = (pri_sem + seg_sem) / 2
# Identificar se passou de ano
if med_ano <= 5:
    # Se o jovem ficou de recuperação
    print('Você REPROVOU!')
    print(f'Tu ficou com a nota de {med_ano:.2f}.')
elif med_ano < 7:
    # Se o jovem ficou abaixo de 7
    print('Você ficou de RECUPERAÇÃO!')
    print(f'Devido a sua nota que foi de {med_ano}.')
elif med_ano < 0:
    print('Algo está errado, tente de novo!')
else:
    # Caso fique assima de 7
    print('Você ficou com a média maior que 7.')
    print(f'TU PASSOU! Com a nota de {med_ano:.2f}.')