# Preço de uma viagem
from time import sleep
from colorama import init
init()
print('\033[33m-=-' * 11)
print('\033[35mPreço da viagem...')
print('\033[33m-=-\033[m' * 11)
# Pergunta a distância
km = str(input('Digite a distância de sua viagem: ')).strip()
km = float(km.split()[0]) # Pega somente o número
print('\033[33m-=-' * 11)
sleep(0.5)
# Time...
print('\033[35mANALISANDO...')
print('\033[33m-=-\033[m' * 11)
sleep(1)
# Calcular preço
if km <= 200: # Para menor ou igual a 200
    preco = km * 0.5 # Cada Km multiplicado por R$0,50
else:
    preco = km * 0.45 # Cada km multiplicado por R$0.45
# Indica o custo
print(f'Sua viagem vai custar: \033[35mR${preco}')
print('\033[33m-=-\033[m' * 11)