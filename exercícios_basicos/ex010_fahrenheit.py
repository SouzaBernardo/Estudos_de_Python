# Transformar grau Celsius para Grau Fahrenheit

# Pedir temp. em °C
grau_cel = str(input('Informe a temperatura em Grau Celsius:')).strip()

# Pegar primeiro número, ignorando coisas como GRAUS
lista = grau_cel.split() # Cria um array com o número e seus complementos
so_numero = lista[0] # Pega somente o número
so_numero = float(so_numero) # Transforma o número em Float

# Aplicar calculos para converter
grau_fah = 9 * so_numero / 5 + 32 # Fahrenheit
kelvin = so_numero + 273.15 # Kelvin

# Resultado...
print(f'A temperatura em Grau Celsius é {so_numero} °C')
print('CONVERTENDO...')
print(f'Temperatura convertida para Grau Fahrenheit: {grau_fah}')
print(f'Temperatura convertida para Kelvin: {kelvin}K')
print('__FIM__')