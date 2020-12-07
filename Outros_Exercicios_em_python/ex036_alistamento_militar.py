# Verificar quando deve se alistar e dar o tempo
print('Vamos ver quando você deve se alistar no exercito?')
# Verificar ano de nascimento
ano_nascimento = input('Qual ano você nasceu?').strip()
# Verificar qual a idade
idade_do_individuo = 2020 - int(ano_nascimento) # Identificar a idade do jovem
tempo_de_alistamento = idade_do_individuo - 18 # Saber quantos anos a pessoa se alistou
# Identificar o caso do individuo
if idade_do_individuo == 18: # Se a pessoa tiver 18 anos
    print('Está na hora de se alistar!')
elif idade_do_individuo > 18: # Se for maior de 18
    print('Você já passou da hora de se alistar!')
    print(f'Seu alistamento foi à {tempo_de_alistamento} anos atrás.')
else:
    # Se for menor de 18
    tempo_de_alistamento = 18 - idade_do_individuo # inverter para o resultado ser +
    print('Este ano você não deve se alistar!')
    print(f'Você deve se alistar daqui a {tempo_de_alistamento} anos.')
print('__FIM__')