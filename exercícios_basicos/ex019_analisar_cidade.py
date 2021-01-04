# Analisar o nome da cidade

nome = str(input('Digite o nome da sua cidade:')).upper().strip() # Saber o nome

# Analisar o nome
if nome.count('SANTO'): # Caso tenha SANTO
    contein = nome.count('SANTO') # Contar quantos SANTOS's tem
    # Resultado
    print('Sua cidade tem em seu nome a palavra "SANTO"!') 
    print(f'Essa palavra aparece {contein} vezes.')
else: # Caso não tenha SANTO
    print('Sua cidade não contém a palavra "SANTO"!') # Resultado
