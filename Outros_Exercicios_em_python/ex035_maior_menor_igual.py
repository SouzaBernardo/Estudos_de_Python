# Pedir dois números e dizer qual deles é maior, menor ou se são iguais 
print('Vamos analisar dois números?!')
print('Primeiro eu preciso que você me diga quais são eles!')
# pedir números
pri_num = input('Primeiro número:')
seg_num = input('Segundo número:')
# Considerar quem é maior e menor
menor = pri_num
maior = pri_num
# Verificar se são diferentes
if seg_num != pri_num:
# Verificar que é maior
    if seg_num < pri_num: #Segundo é menor?
        menor = seg_num
        print('O primeiro número é maior')
    else:
        maior = seg_num #Se o segundo não é menor, ele é maior
        print('O segundo número é maior')
    print(f'=-= O número maior é {maior}.=-=')
    print(f'=-=O menor número é {menor}.=-=')
else:
    print('Os números são iguais!')
# Resposta
print('__FIM__')