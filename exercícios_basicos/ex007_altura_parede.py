# Quantos litros de tinta para pintar a área da parede
# 1L == 2m²
print('\033[33mVAMOS PINTAR A PAREDE!!!\033[m')
alt = float(input('Altura da parede:'))
lag = float(input('Largura da parede:'))
area = alt * lag / 2 
tinta = area / 2 # calcula a quantidade de tinta
print(f'A área é \033[33m{area}m²\033[m e precisará \033[33m{tinta}L de tinta\033[m para pinta-la.')
print('__FIM__')
