# Verificar quando deve se alistar e dar o tempo

from datetime import date # importar tempo do sistema
ano_atual = date.today().year # data do pc, hoje().ano

cores = {
    'limpo': '\033[m',
    'vermelho': '\033[31m',
    'verde':'\033[32m',
    'amarelo': '\033[33m',
}

linha = f'{cores["amarelo"]}-=' * 26 + f'{cores["limpo"]}'

print(linha)
print(f'{cores["amarelo"]}Vamos ver quando você deve se alistar no exercito?{cores["limpo"]}')

ano_nascimento = int(input('Qual ano você nasceu?'))
idade_do_individuo = int(ano_atual) - ano_nascimento
tempo_de_alistamento = idade_do_individuo - 18 

print(linha)
print(f'{cores["verde"]}Quem nasceu em {ano_nascimento} tem ou terá {idade_do_individuo} anos em {ano_atual}{cores["limpo"]}')
print(linha)

if idade_do_individuo > 18: 
    if idade_do_individuo == 18:
        print('Está na hora de se alistar!')
    else:
        print(f'{cores["vermelho"]}Você já passou da hora de se alistar!{cores["limpo"]}')
        print(f'Seu alistamento foi há {cores["vermelho"]}{tempo_de_alistamento}{cores["limpo"]} anos atrás.')
else:
    tempo_de_alistamento = 18 - idade_do_individuo 
    ano_alistamento = ano_atual + tempo_de_alistamento
    print(f'Este ano {cores["vermelho"]}você não deve se alistar{cores["limpo"]}!')
    print(f'Você deve se alistar {cores["vermelho"]}daqui a {tempo_de_alistamento} anos{cores["limpo"]}, em {cores["vermelho"]}{ano_alistamento}{cores["limpo"]}.')
print(linha)