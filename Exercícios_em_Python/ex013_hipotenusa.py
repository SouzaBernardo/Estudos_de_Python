# Calcular a hipotenusa
from math import hypot
cA = float(input('Cateto adjacente:'))
cO = float(input('Cateto oposto:'))
#H = (cA ** 2 + cO ** 2) ** (1/2)
H = hypot(cA, cO) #metodo math
print('A hipotenusa, do cateto oposto de valor {} e cateto adjacente de valor {}, é: {:.2f}'.format(cO, cA, H))
