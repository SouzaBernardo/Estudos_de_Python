# Dizer o dobro, triblo e a raiz de um número INTEIRO...
num = int(input('Digite um número:')) # Pede o número INTEIRO

# Calcular o dobro, triplo e raiz...
dobro = num * 2
triplo = num * 3 
raiz = num ** (1/2)

# Dizer o resultado...
print('Seu número escolhido foi {}.'.format(num))
print('O DOBRO dele é {}'.format(dobro))
print('Já, seu triplo é {}'.format(triplo))
print('Por fim, a sua raiz é {}'.format(raiz))