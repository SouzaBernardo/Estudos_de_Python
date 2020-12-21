# Identificar ano bissexto
from colorama import init
init()
print('\033[33m-=-\033[m' * 8)
ano = int(input('Qual ano que você está? ')) # Pedir o ano
print('\033[33m-=-' * 8)
# Verificar se é ou não bissexto
if ano % 4 == 0:
    print('\033[mVocê \033[32mestá\033[m em um ano \033[33mbissexto.\033[m')
else:
    print('\033[mVocê \033[31mnão\033[m está em um ano \033[33mbissexto.\033[m')
# Fim
print('\033[33m-=-' * 8)
print('\033[31m_FIM_')
