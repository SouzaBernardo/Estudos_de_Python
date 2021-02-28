# Dizer o dobro, triblo e a raiz de um número INTEIRO...
cores = {
    'sem_cor':'\033[m',
    'amarelo':'\033[33m',
    'vermelho':'\033[31m',
    'azul':'\033[34m',
    'verde':'\033[32m'
}
num = int(input('Digite um número:'))
dobro = num * 2
triplo = num * 3 
raiz = num ** (1/2)
# resultados
print(f'Seu número escolhido foi {cores["amarelo"]}{num}{cores["sem_cor"]}.')
print(f'O DOBRO dele é {cores["vermelho"]}{dobro}{cores["sem_cor"]}')
print(f'Já, seu triplo é {cores["azul"]}{triplo}{cores["sem_cor"]}')
print(f'Por fim, a sua raiz é {cores["verde"]}{raiz:.2f}{cores["sem_cor"]}')
