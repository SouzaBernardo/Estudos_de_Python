km = float(input('Digite a distância de sua viagem:'))
if km <= 200:
    pe = km * 0.5
    print('Sua viagem vai custar {}'.format(pe))
else:
    pa = km * 0.45
    print('Sua viagem vai custar {}'.format(pa))
