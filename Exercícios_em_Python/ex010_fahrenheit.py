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

print(grau_cel, lista, so_numero, grau_fah, kelvin)