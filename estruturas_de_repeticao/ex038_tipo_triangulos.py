# Verificar se as retas formam um triangulo, se sim, qual?
cores = {
    'limpo':'\033[m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'azul':'\033[34m',
}

linha = f'{cores["amarelo"]}-=' * 30 + f'{cores["limpo"]}'

print(linha)
print(f'{cores["amarelo"]}Vamos analisar 3 retas? preciso saber a medida delas!{cores["limpo"]}')

print(linha)
pri_reta = input('Medida da primeira reta:').strip().split()
seg_reta = input('Medida da segunda reta:').strip().split()
ter_reta = input('Medida da terceira reta:').strip().split()
print(linha)
      
pri_reta = float(pri_reta[0])
seg_reta = float(seg_reta[0])
ter_reta = float(ter_reta[0])
# menor
if seg_reta < pri_reta and seg_reta < ter_reta:
    menor = seg_reta
elif ter_reta < pri_reta and ter_reta < seg_reta:
    menor = ter_reta
else:
    menor = pri_reta
# maior
if seg_reta > pri_reta and seg_reta > ter_reta:
    maior = seg_reta 
elif ter_reta > pri_reta and ter_reta > seg_reta:
    maior = ter_reta 
else:
    maior = pri_reta
# medio
if seg_reta > menor and seg_reta < maior:
    media = seg_reta
elif ter_reta > menor and ter_reta < maior:
    media = ter_reta
else:
    media = pri_reta

if menor + media > maior:
    # Equilatero(=TUDO IGUAL=), Escaleno(!TUDO DIFERENTE=)

    equilatero = pri_reta == seg_reta and pri_reta == ter_reta
    escaleno = pri_reta != seg_reta and pri_reta != ter_reta and seg_reta != ter_reta
    
    if equilatero == True:
        print('Este triangulo é um equilatero')
    elif escaleno == True: 
        print('Este é um triangulo escaleno')
    else:
        print('Este é um triangulo isoceles')
else: 
    print('NÃO forma um triangulo')
print(linha)
