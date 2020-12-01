# Analisar se há multa

# Pedir nome
print('Vamos analisar seu perfil para ver se há multa...')
print('ANALISANDO...')
speed = input('Qual a velocidade que seu carro ultrapassou:').strip().upper()

# Analisar
nume = speed.split()  # Dividir as palavras em uma lista
numero = float(nume[0]) # Pegar [0](que é o número) e tranforma para float

print(f'Você passou a {numero} km/h.') # Indica a sua velocidade

if numero >= 80.0: # Caso tenha ultrapassado o limite
    multa = (numero - 80) * 7 # Aplica a multa
    print('Você tem uma multa!') # Indica a multa
    print('Ultrapassou o limite de 80Km/h.') # Indica o limite de velocidade
    print(f'Ela custa R${multa}.') # Mostra a multa
else: # Caso NÃO tenha ultrapassado o limite
    print('Tudo certo!')
    print('Não ultramasse 80km/h.')
    
# FIM
print('Lembre de usar cinto de segurança!')
print('__FIM__')
