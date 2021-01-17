# Analisar se há multa
from time import sleep

cores = {
    'limpo':'\033[m',
    'amarelo':'\033[33m',
    'vermelho':'\033[31m',
    'azul_claro':'\033[36m',
    'verde':'\033[32m'
}

linha_amarela = f'{cores["amarelo"]}-=-' * 15 + f'{cores["limpo"]}'

print(linha_amarela)
print(f'{cores["vermelho"]}Caso seja número quebrado, use PONTO ao invés de virgula!')
print('Use somente números, sem KM/h, por exemplo.') # não aceita outra coisa além de números

print(f'{cores["amarelo"]}')
speed = float(input('Qual a velocidade que seu carro ultrapassou: '))
print(f'{cores["limpo"]}')

sleep(1)
print(linha_amarela)
print('\033[32mANALISANDO...')
print(linha_amarela)
sleep(1)

if speed > 80.0:
    multa = (speed - 80) * 7 # Calcular a multa
    print(f'Você tem uma {cores["vermelho"]}multa!{cores["azul_claro"]} Ultrapassou o limite de 80Km/h.')
    print(f'Ela custa {cores["vermelho"]}R${multa:.2f}!{cores["limpo"]}')
elif speed == 80.0:
    print(f'{cores["vermelho"]}CUIDADO!')
    print(f'Você passou no {cores["azul_claro"]}LIMITE!')
    print(f'{cores["azul_claro"]}MULTA NÃO APLICADA')
else:
    print(f'{cores["verde"]}Tudo certo!')
    print(f'Não ultramasse 80km/h.{cores["limpo"]}')

print(linha_amarela)
print(f'{cores["verde"]}Lembre de usar cinto de segurança!')
print(linha_amarela)
print(f'{cores["vermelho"]}__FIM__{cores["limpo"]}')
