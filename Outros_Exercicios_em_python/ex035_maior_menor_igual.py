from colorama import init
init()
# Pedir dois números e dizer qual deles é maior, menor ou se são iguais 
print('\033[31mVamos analisar dois números?!\033[m')
print('Primeiro eu preciso que você me diga quais são eles!')
# pedir números
pri_num = input('Primeiro número:')
seg_num = input('Segundo número:')
# Considerar quem é maior e menor
color = '\033[33m=-=\033[m'
menor = pri_num
maior = pri_num
# Verificar se são diferentes
if seg_num != pri_num:
# Verificar que é maior
    if seg_num < pri_num: #Segundo é menor?
        menor = seg_num
        print('O \033[31mprimeiro\033[m número é \033[31mmaior\033[m')
    else:
        maior = seg_num #Se o segundo não é menor, ele é maior
        print('O \033[31msegundo\033[m número é \033[31mmaior\033[m')
    print(f'{color} O número \033[34mmaior\033[m é \033[34m{maior}\033[m. {color}')
    print(f'{color} O  número \033[32mmenor\033[m é \033[32m{menor}\033[m. {color}')
else:
    print('Os números \033[31msão iguais\033[m!')
# Resposta
print('\033[31m__FIM__\033[m')