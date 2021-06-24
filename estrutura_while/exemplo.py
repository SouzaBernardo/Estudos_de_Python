# Aula 14 ------
'''
    - Estrutura sem limite, deferente do for 
        - não exige saber a posição
    - quando não se sabe a quantidade, usamos o for, até a situação for Verdadeira
    - while verifica no inicio se é F ou V

# exemplo de for dado antes
for c in range(1, 10):
    print(c)
print('FIM')
'''
c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')