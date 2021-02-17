# Calcular o IMC de uma pessoa
cores = {
    'limpo':'\033[m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'azul':'\033[34m',
}# arrumar as cores
print('Vamos calcular seu IMC!')

peso_kg = str(input('Preciso saber seu peso, em Quilogramas: ')).strip()
alt_metros = str(input('Agora, preciso saber sua altura, em metros: ')).strip()

peso_kg = float(peso_kg.split()[0])
alt_metros = float(alt_metros.split()[0])

imc_pessoa = peso_kg / (alt_metros ** 2)

imc_class = 'Peso Baixo'

if imc_pessoa >= 18.5 or imc_pessoa <= 24.9:
    imc_class = 'Peso Normal'
elif imc_pessoa >= 25 or imc_pessoa <= 29.9:
    imc_class = 'Sobre Peso'
elif imc_pessoa >= 30 or imc_pessoa <= 34.9:
     imc_class = 'Obesidade (Grau I)'
elif imc_pessoa >= 35 or imc_pessoa <= 39.9:
    imc_class = 'Obesidade Severa (Grau II)'
else:
    imc_class = 'Obesidade Mórbida (Grau III)'
print(f'Seu peso é {imc_pessoa} e sua classificação é {imc_class}')
