# Quantos litros de tinta para pintar a área da parede
# 1L == 2m²

# Pedir altura e lagura
alt = float(input('Altura da parede:'))
lag = float(input('Largura da parede:'))
# Calcular a área e a necessidade de litros
area = alt * lag / 2 # área
tinta = area / 2 # litros para pintar
# Dizer resultado
print(f'A área é {area}m² e precisará {tinta}L de tinta')
