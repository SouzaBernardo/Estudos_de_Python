# Pedir um número e dizer seu sucessor e antecessor
cores = {
    'sem_cor':'\033[m',
    'amarelo':'\033[33m',
    'vermelho':'\033[31m',
    'azul':'\033[34m'
}
numero = int(input(f'{cores["amarelo"]}Digite um número inteiro:'))
sucessor = numero + 1 
antecessor = numero - 1 
print('=/' * 9 + f'={cores["sem_cor"]}')
print(f'Seu número foi {cores["amarelo"]}{numero}{cores["sem_cor"]};')
print(f'O {cores["vermelho"]}antecessor{cores["sem_cor"]} desse número é {cores["vermelho"]}{antecessor}{cores["sem_cor"]};')
print(f'O {cores["azul"]}sucessor{cores["sem_cor"]} é {cores["azul"]}{sucessor}{cores["amarelo"]}.') 
print('=/' * 9 + '=')
print(f'__FIM__{cores["sem_cor"]}')