# Transformar grau Celsius para Grau Fahrenheit

# Pedir temp. em °C
grau_fah = str(input('Informe a temperatura em °C:')).upper().strip()

# Ignorar '°C' ou 'Grau' ou 'Celsius' ou 'Celsios'

if grau_fah.count('°C'):
    # Substiui °C por '' -> espaço vazio
    grau_fah = grau_fah.replace('°C', '')

if grau_fah.count('GRAU CELSIUS'):
    # Substiui Grau Celsius por '' -> espaço vazio
    grau_fah = grau_fah.replace('GRAU CELSIUS', '')

if grau_fah.count('GRAUS CELSIUS'):
    # Substitui Graus
    grau_fah = grau_fah.replace('')
if grau_fah.count('GRAUS'):
    grau_fah = grau_fah.replace('')
if grau_fah.count('GRAUS CELSIOS'):
    grau_fah = grau_fah.replace('')
print(grau_fah)