# Analisar se há multa
from time import sleep
from colorama import init
init()
# Pedir velocidade
print('\033[33m-=-\033[m' * 15)
speed = input('Qual a velocidade que seu carro ultrapassou: ').strip()
if speed.count(','): # Indicar que o usuário ñ pode usar vírgula
    print('\033[31mERRO!')
    print('\033[mNão use VÍRGULA. Use PONTO')
else: # Caso o usuário ñ use vírgula
    numero = float(speed.split()[0]) # Transforma o primeiro objeto em float
# Time (Dar tempo para processar)
print('\033[33m-=-\033[m' * 15)
print('\033[32mANALISANDO...')
sleep(2)
print('\033[33m-=-\033[m' * 15)
# Analisar se há multa
if numero > 80.0: # Caso tenha ultrapassado o limite
    multa = (numero - 80) * 7 # Calcular a multa
    print('\033[31mVocê tem uma \033[36mmulta!\033[31m Ultrapassou o limite de 80Km/h.') # Indica o limite de velocidade
    print(f'Ela custa \033[36mR${multa:.2f}!\033[m') # Mostra a multa
elif numero == 80.0: # Caso seja 80 km ñ tem multa, mas dá um aviso
    print('\033[31mCUIDADO!')
    print('Você passou no \033[34mLIMITE!')
    print('\033[32mMULTA NÃO APLICADA')
else: # Caso NÃO tenha ultrapassado o limite
    print('\033[32mTudo certo!') # Dar o OK
    print('Não ultramasse 80km/h.\033[m')
# FIM
print('\033[33m-=-' * 15) # Linha amarela
print('\033[32mLembre de usar cinto de segurança!') # Linha verde, use cinto
print('\033[33m-=-' * 15)
print('\033[31m__FIM__\033[m') # Fim vermelho
