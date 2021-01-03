# Verificar quando deve se alistar e dar o tempo
from datetime import date # importar tempo do sistema
ano_atual = date.today().year # data do pc, hoje().ano
print('\033[33mVamos ver quando você deve se alistar no exercito?\033[m')
# ano de nascimento
ano_nascimento = int(input('Qual ano você nasceu?'))
# qual a idade
idade_do_individuo = int(ano_atual) - ano_nascimento # Identificar a idade do jovem
tempo_de_alistamento = idade_do_individuo - 18 # Saber quantos anos a pessoa se alistou
# indicar a situação do individuo
print('\033[31m-=\033[m' * 10)
print(f'Quem nasceu em {ano_nascimento} tem ou terá {idade_do_individuo} anos em {ano_atual}')
print('\033[31m-=\033[m' * 10)
# Maior de idade anos
if idade_do_individuo > 18: 
    if idade_do_individuo == 18:
        print('Está na hora de se alistar!')
    else: # Se for maior de 18
        print('Você já passou da hora de se alistar!')
        print(f'Seu alistamento foi há {tempo_de_alistamento} anos atrás.')
else:
    # Se for menor de 18
    tempo_de_alistamento = 18 - idade_do_individuo # inverter para o resultado ser +
    ano_alistamento = ano_atual + tempo_de_alistamento
    print('Este ano você não deve se alistar!')
    print(f'Você deve se alistar daqui a {tempo_de_alistamento} anos, em {ano_alistamento}.')
print('__FIM__')