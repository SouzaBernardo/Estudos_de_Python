# Calcular o IMC de uma pessoa
'''Peso (em kg) - Com auxílio de uma balança, meça o seu peso corporal em kilogramas e anote o valor. Por exemplo: 82.
    Altura (em metros) - Com auxílio de uma fita métrica, meça a sua altura em metros e anote o valor. Por exemplo: 1,76.
    Altura ao quadrado - Com auxílio de uma calculadora, calcule o valor da sua altura ao quadrado e anote o valor. O jeito mais fácil é multiplicar o valor da altura por ele mesmo. Por exemplo: 1,76 x 1,76 = 3,0976.
    Resultado do IMC - Com auxílio da calculadora, divida o valor do seu peso pelo valor da sua altura ao quadrado. Por exemplo: 82 ÷ 3,0976 = 26,472.
    Tabela IMC - Confira a tabela do IMC para saber se você está abaixo do peso, dentro do peso ou com sobrepeso. Por exemplo: O IMC 26,472 indica uma pessoa acima do peso.
'''
print('Vamos calcular seu IMC!')
peso_kg = str(input('Preciso saber seu peso, em Quilogramas: ').strip().split())
alt_metros = str(input('Agora, preciso saber sua altura, em metros: ').strip().split())
# Verificar se podemos transformar para números
if peso_kg.count(',') or alt_metros.count(','):
    print('ERRO, você usou virgula. Substitu-a por ponto!') # informar que deve ter Ponto
else:
    # Transform to Float
    peso_kg = float(peso_kg[0])
    alt_metros = float(alt_metros[0])
    # Calcula IMC
    imc_pessoa = peso_kg / (alt_metros**2)
    # Falta verificar na tabela