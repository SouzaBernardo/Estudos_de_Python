print('Vamos analisar seu perfil para ver se há multa...')
print('ANALISANDO...')
speed = input('Qual a velocidade que seu carro ultrapassou:').strip().upper()
nume = speed.split()
numero = int(nume[0])
multa = (numero - 80) * 7
print('Você passou a {} km/h'.format(numero))
if numero >= 80:
    print('Você tem uma multa!')
    print('E ela custa R${}, devido a sua velocidade que foi de {}Km/h.'.format(multa, numero))
else:
    print('Tudo certo!')
    print('Não ultramasse 80km/h')
print('Lembre de usar cinto de segurança!')
print('__<_FIM_>__')
