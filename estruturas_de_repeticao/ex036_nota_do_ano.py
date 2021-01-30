# Dizer a média anual de um aluno e dizer se ele passou.
cores = {
    'limpa':'\033[m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'azul':'\033[34m',
}
print(f'{cores["verde"]}BOLETIM:{cores["limpo"]}')
print('Para saber se você passou, preciso das suas notas do 1° e 2° semestre...')

pri_sem = float(input('Primeiro semestre:'))
seg_sem = float(input('Segundo semestre:'))
med_ano = (pri_sem + seg_sem) / 2

if med_ano <= 5:
    print(f'Você {cores["vermelho"]}REPROVOU{cores["limpo"]}!')
    print(f'Tu ficou com a nota de {cores["vermelho"]}{med_ano:.2f}{cores["limpo"]}.')
elif med_ano < 7:
    print(f'Você ficou de {cores["vermelho"]}RECUPERAÇÃO{cores["limpo"]}!')
    print(f'Devido a sua nota que foi de {cores["vermelho"]}{med_ano}{cores["limpo"]}.')
elif med_ano < 0:
    print(f'{cores["vermelho"]}Algo está errado, tente de novo!{cores["limpo"]}')
else:
    print(f'Você ficou com a {cores["verde"]}média maior que 7{cores["limpo"]}.')
    print(f'TU PASSOU! Com a nota de {cores["verde"]}{med_ano:.2f}{cores["limpo"]}.')
