'''
- ler ano de nacimento de 7 pessoas
- dizer quantos são maiores de 21 anos
'''

from datetime import date, timedelta

# ano do sistema...
data_atual = date.today()
ano_atual = int(data_atual.year)
maiores_de_21 = 0

for i in range(0, 7):
    # idade do individuo
    data_nascimento = int(input('Data de nascimento:'))
    idade = ano_atual - data_nascimento # calcula a idade comparando com o sistema
    
    if idade >= 21:
        maiores_de_21 += 1
    

print(f'Há {maiores_de_21} pessoas maiores de idade nesse grupo!')

