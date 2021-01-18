# Descobrir qual número é maior, menor e o do meio
cores = {
    'limpo':'\033[m',
    'vermelho':'\033[31m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'azul':'\033[34m',
}

linha_amarela = f'{cores["amarelo"]}-=-' * 10 + f'{cores["limpo"]}'
opcoes = [f'{cores["vermelho"]}Primeiro{cores["limpo"]}', f'{cores["verde"]}Segundo{cores["limpo"]}', f'{cores["azul"]}Terceiro{cores["limpo"]}']

print(linha_amarela)
print('Diga-me 3 números e vou dizer qual deles é maior, menor, medio e a ordem crescente!')

print(f'{cores["vermelho"]}')
n1 = float(input('Primeiro:'))
print(f'{cores["limpo"]}')

print(linha_amarela)

print(f'{cores["verde"]}')
n2 = float(input('Segundo:'))
print(f'{cores["limpo"]}')

print(linha_amarela)

print(f'{cores["azul"]}')
n3 = float(input('Terceiro:'))
print(f'{cores["limpo"]}')

print(linha_amarela)
if n1 == n2 and n1 == n3:
    print(f'{cores["amarelo"]}TODOS SÃO IGUAIS!!!{cores["limpo"]}')
else:
    if n2 < n1 and n2 < n3:
        menor = n2
        menor_str = opcoes[1]
    elif n3 < n1 and n3 < n2:
        menor = n3
        menor_str = opcoes[2]
    else:
        menor = n1
        menor_str = opcoes[0]

    if n2 > n1 and n2 > n3:
        maior = n2
        maior_str = opcoes[1]
    elif n3 > n2 and n3 > n1:
        maior = n3
        maior_str = opcoes[2]
    else:
        maior = n1
        maior_str = opcoes[0]

    if n2 > menor and n2 < maior:
        meio = n2
        meio_str = opcoes[1]
    elif n3 > menor and n3 < maior:
        meio = n3
        meio_str = opcoes[2]
    else:
        meio = n1
        meio_str = opcoes[0]
    print(f'O menor é o {menor_str}({menor}).')
    print(f'o número mediano é {meio_str}({meio}).')
    print(f'O maior é {maior_str}({maior}).')
    print(f'A ordem crescente é {menor_str}({menor}), {meio_str}({meio}), {maior_str}({maior}).')
 