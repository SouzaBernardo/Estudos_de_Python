'''
- nome, idade e sexo => 4 pessoas
    ## mostrar
        -media da idade 
        -mais velho
        -quantas mulheres menores de 20anos
'''
#média ok

soma_idades = 0
media = 0
for i in range(1, 5):
    nome = str(input('Digite o nome:'))
    idade = int(input('Digite a idade:'))
    sexo = str(input('Digite o sexo (M/F):')).upper()
    
    # identificar quem é mais velho
    if i == 1:
        mais_velho = nome, idade, sexo
    else:
        if idade > mais_velho[1]:
            mais_velho = nome, idade, sexo

    soma_idades += idade

media = soma_idades / 4

print(f'A media das idades foi: {media}')
print(mais_velho)