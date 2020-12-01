# Preço de uma viagem
km = float(input('Digite a distância de sua viagem:')) # Pergunta a distância
if km <= 200: # Para menor ou igual a 200
    pe = km * 0.5 # Cada Km multiplicado por R$0,50
    print(f'Sua viagem vai custar R${pe}.') # Indica o custo
else:
    pa = km * 0.45 # Cada km multiplicado por R$0.45
    print(f'Sua viagem vai custar R${pa}.')
