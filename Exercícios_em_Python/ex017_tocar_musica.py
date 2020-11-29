# Escolher e tocar a música
from pygame import mixer

print('Escolha a música que quer tocar:')
print('Música 1: - Drop - Anno Domini Beats')
print('Música 2: - Forever -Anno Domini Beats ')
print('Música 3: - Cash Machine -Anno Domini Beats')
escolha = input('Qual a sua escolha (somente o número)?')
if escolha != '1':
    mixer.init()
    mixer.music.load('ex017-drop.mp3')
    mixer.music.play()
    while(mixer.music.get_busy()): pass
