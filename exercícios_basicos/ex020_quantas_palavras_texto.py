# Quantas palavras tem em um texto

# Pedir palavra
palavra = str(input('Qual palavra você quer saber a quantidade?'))

# Pedir texto
print('DIGITE O TEXTO ABAIXO:')
texto = str(input(''))

quantidade_palavra = texto.count(palavra) # Analisar quantas palavras tem

# Resultado
print(f'A palavra {palavra} no seu texto repete {quantidade_palavra} vezes.')