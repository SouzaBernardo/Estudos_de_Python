# Realizar a média anual de um aluno...
cores = {
    'sem_cor':'\033[m',
    'amarelo':'\033[33m',
    'vermelho':'\033[31m',
    'azul':'\033[34m',
    'verde':'\033[32m'
}
print(f'{cores["amarelo"]}Olá, vamos descobrir a sua média no ano?{cores["sem_cor"]}') # Dar olá para pessoa
primeira_nota = float(input(f'Qual a sua nota {cores["amarelo"]}TOTAL{cores["sem_cor"]} do {cores["amarelo"]}primeiro semestre{cores["sem_cor"]}?'))
segunda_nota = float(input(f'E a do {cores["azul"]}segundo semestre{cores["sem_cor"]}? Qual a sua nota?'))
media_resposta = (primeira_nota + segunda_nota) / 2 # calculo da media

print(F'Sua nota do {cores["amarelo"]}primeiro semestre{cores["sem_cor"]} foi {cores["amarelo"]}{primeira_nota:.1f}{cores["sem_cor"]}')
print(f'E, sua nota do {cores["azul"]}segundo semestre{cores["sem_cor"]} foi {cores["azul"]}{segunda_nota:.1f}{cores["sem_cor"]}')
print(f'Portanto, sua {cores["verde"]}media{cores["sem_cor"]} deste ano foi {cores["verde"]}{media_resposta:.1f}{cores["sem_cor"]}.')
if media_resposta >= 7:
    print(f'{cores["verde"]}APROVADO!!!{cores["sem_cor"]}')
else:
    print(f'Você está de {cores["vermelho"]}RECUPERAÇÃO{cores["sem_cor"]}.')
print('__FIM__')