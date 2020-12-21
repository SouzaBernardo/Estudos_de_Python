# Preço de uma viagem
from time import sleep
print('-=-' * 11)
print('Preço da viagem')
print('-=-' * 11)
# Pergunta a distância
km = str(input('Digite a distância de sua viagem: ')).strip()
km = float(km.split()[0]) # Pega somente o número
print('-=-' * 11)
sleep(0.5)
# Time...
print('ANALISANDO...')
print('-=-' * 11)
sleep(1)
# Calcular preço
if km <= 200: # Para menor ou igual a 200
    pe = km * 0.5 # Cada Km multiplicado por R$0,50
    print(f'Sua viagem vai custar R${pe}.') # Indica o custo
else:
    pa = km * 0.45 # Cada km multiplicado por R$0.45
    print(f'Sua viagem vai custar R${pa}.')
print('-=-' * 11)