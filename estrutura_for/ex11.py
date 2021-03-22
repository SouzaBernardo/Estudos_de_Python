'''
- nome, idade e sexo => 4 pessoas
    ## mostrar
        -media da idade 
        -mais velho
        -quantas mulheres menores de 20anos
'''
#média ok

total_idade = 0
media = 0
for i in range(1, 5):
    #nome = str(input('Digite o nome:'))
    idade = int(input('Digite a idade:'))
    #sexo = str(input('Digite o sexo (M/F):'))
    total_idade += idade
    
media = total_idade / 4
print(f'A media das idades foi: {media}')