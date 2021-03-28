'''
- nome, idade e sexo => 4 pessoas
    ## mostrar
        -media da idade 
        -mais velho
        -quantas mulheres menores de 21anos
'''
#média ok

soma_idades = 0
media = 0
mulheres_menores_21 =0


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

    # verificar a quantidade de mulheres menores de 21 anos
    if mais_velho.count('F') and idade < 21:
        mulheres_menores_21 += 1

    soma_idades += idade

media = soma_idades / 4

print(f'A media das idades foi: {media}')
print(f'Há {mulheres_menores_21} mulheres menores de 21 anos')
print(f'A pessoa mais velha é {mais_velho[0]} com {mais_velho[1]}')