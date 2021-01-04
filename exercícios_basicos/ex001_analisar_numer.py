# Pedir um número e dizer seu sucessor e antecessor
numero = int(input('\033[33mDigite um número inteiro:\033[m'))
sucessor = numero + 1 
antecessor = numero - 1 
# cores
sem_cor = '\033[m'
amarelo = '\033[33m'
vermelho = '\033[31m'
azul = '\033[34m'
print('=/' * 9 + '=')
print(f'Seu número foi {amarelo}{numero}{sem_cor};')
print(f'O {vermelho}antecessor{sem_cor} desse número é {vermelho}{antecessor}{sem_cor};')
print(f'O {azul}sucessor{sem_cor} é {azul}{sucessor}{sem_cor}.') 
print('=/' * 9 + '=')
print('\033[33m__FIM__\033[m')