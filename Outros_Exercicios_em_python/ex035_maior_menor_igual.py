# Pedir dois números e dizer qual deles é maior, menor ou se são iguais 
print('Vamos analisar dois números?!')
print('Primeiro eu preciso que você me diga quais são eles!')
# pedir números
pri_num = input('Primeiro número:')
seg_num = input('Segundo número:')
# Considerar quem é maior e menor
menor = pri_num
maior = pri_num
# Verificar que é maior
if seg_num < pri_num: # Verificar se 
    menor = seg_num
elif seg_num == pri_num: # Verificar se são iguais
    print('Os números são iquais')
else:
    maior = seg_num # Verificar se o segundo é maior
# Resposta
print(f'O número maior é {maior} e o menor é {menor}.')
print('__FIM__')