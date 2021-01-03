# Verificar quando deve se alistar e dar o tempo
print('Vamos ver quando você deve se alistar no exercito?')
# Verificar ano de nascimento
ano_nascimento = int(input('Qual ano você nasceu?'))
# Verificar qual a idade
idade_do_individuo = 2020 - ano_nascimento # Identificar a idade do jovem
tempo_de_alistamento = idade_do_individuo - 18 # Saber quantos anos a pessoa se alistou
# Identificar o caso do individuo
print('-=' * 10)
print(f'Quem nasceu em {ano_nascimento} tem {idade_do_individuo} anos em 2020')
print('-=' * 10)
# Maior de idade anos
if idade_do_individuo > 18: 
    if idade_do_individuo == 18:
        print('Está na hora de se alistar!')
    else: # Se for maior de 18
        print('Você já passou da hora de se alistar!')
        print(f'Seu alistamento foi à {tempo_de_alistamento} anos atrás.')
else:
    # Se for menor de 18
    tempo_de_alistamento = 18 - idade_do_individuo # inverter para o resultado ser +
    ano_alistamento = 2020 + tempo_de_alistamento
    print('Este ano você não deve se alistar!')
    print(f'Você deve se alistar daqui a {tempo_de_alistamento} anos, em {ano_alistamento}.')
print('__FIM__')