# Dizer a média anual de um aluno e dizer se ele passou.
cores = {
    'limpa':'\033[m',
    'azul':'\033[34m',
    'amarelo':'\033[33m',
    'verde':'\033[32m'
}
print('\033[32mBOLETIM:\033[m')
print('Para saber se você passou, preciso das suas notas do 1° e 2° semestre...')

pri_sem = float(input('Primeiro semestre:'))
seg_sem = float(input('Segundo semestre:'))
med_ano = (pri_sem + seg_sem) / 2

if med_ano <= 5:
    print('Você \033[31mREPROVOU\033[m!')
    print(f'Tu ficou com a nota de \033[31m{med_ano:.2f}\033[m.')
elif med_ano < 7:
    print('Você ficou de \033[31mRECUPERAÇÃO\033[m!')
    print(f'Devido a sua nota que foi de \033[31m{med_ano}\033[m.')
elif med_ano < 0:
    print('\033[31mAlgo está errado, tente de novo!\033[m')
else:
    print('Você ficou com a \033[32mmédia maior que 7\033[m.')
    print(f'TU PASSOU! Com a nota de \033[32m{med_ano:.2f}\033[m.')
