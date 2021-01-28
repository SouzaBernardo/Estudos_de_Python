# Calcular o IMC de uma pessoa
cores = {
    'limpa':'\033[m',
    'azul':'\033[34m',
    'amarelo':'\033[33m',
    'verde':'\033[32m'
}
print('Vamos calcular seu IMC!')

peso_kg = str(input('Preciso saber seu peso, em Quilogramas: ')).strip()
alt_metros = str(input('Agora, preciso saber sua altura, em metros: ')).strip()

peso_kg = float(peso_kg.split()[0])
alt_metros = float(alt_metros.split()[0])

imc_pessoa = peso_kg / (alt_metros ** 2)

if imc_pessoa < 18.5:
    print('Peso Baixo')
elif imc_pessoa >= 18.5 or imc_pessoa <= 24.9:
    print('Peso Normal')
elif imc_pessoa >= 25 or imc_pessoa <= 29.9:
    print('Sobre Peso')
elif imc_pessoa >= 30 or imc_pessoa <= 34.9:
     print('Obesidade (Grau I)')
elif imc_pessoa >= 35 or imc_pessoa <= 39.9:
    print('Obesidade Severa (Grau II)')
else:
    print('Obesidade Mórbida (Grau III)')
