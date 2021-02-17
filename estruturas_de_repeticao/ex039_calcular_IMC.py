# Calcular o IMC de uma pessoa
cores = {
    'limpo':'\033[m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'azul':'\033[34m',
}# arrumar as cores
linha = f'{cores["amarelo"]}-=' * 22 + f'{cores["limpo"]}'

print(linha)
print('Vamos calcular seu IMC!')
print(linha)

peso_kg = str(input('Preciso saber seu peso, em Quilogramas: ')).strip()
alt_metros = str(input('Agora, preciso saber sua altura, em metros: ')).strip()

print(linha)

peso_kg = float(peso_kg.split()[0])
alt_metros = float(alt_metros.split()[0])

imc_pessoa = peso_kg / (alt_metros ** 2)

if imc_pessoa >= 0 and imc_pessoa < 18.5:
    imc_class = 'Peso Baixo'
elif imc_pessoa >= 18.5 and imc_pessoa <= 24.9:
    imc_class = 'Peso Normal'
elif imc_pessoa >= 25 and imc_pessoa <= 29.9:
    imc_class = 'Sobre Peso'
elif imc_pessoa >= 30 and imc_pessoa <= 34.9:
     imc_class = 'Obesidade (Grau I)'
elif imc_pessoa >= 35 and imc_pessoa <= 39.9:
    imc_class = 'Obesidade Severa (Grau II)'
else:
    imc_class = 'Obesidade Mórbida (Grau III)'

print(f'Seu IMC é {imc_pessoa:.2f} e sua classificação é {imc_class}')
print(linha)
