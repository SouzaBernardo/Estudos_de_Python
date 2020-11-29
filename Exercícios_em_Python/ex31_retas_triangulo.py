# Saber se as 3 retas fazem um riangulo
reta1 = float(input('Comprimento da primeira reta:')) # Priemira reta
reta2 = float(input('Comprimento da segunda reta:')) # Segunda reta
reta3 = float(input('Comprimento da terceira reta:')) # Terceira reta

# definir um padrão para maior e menor

menor = reta1 # considera a reta1 a menor -> temporario
medio = reta1 # quem é o numero do meio
maior = reta1 # considera a reta1 a maior -> temporario


# analisar qual é a reta menor

if reta2 < reta1 and reta2 < reta3: 
    menor = reta2
if reta3 < reta1 and reta3 < reta2:
    menor = reta3

# analisar qual é a reta maior

if reta2 > reta1 and reta2 > reta3:
    maior = reta2
if reta3 > reta1 and reta3 > reta2:
    maior = reta3

# analisar quem é o medio

if reta2 < maior and reta2 > menor:
    medio = reta2
if reta3 < maior and reta3 > menor:
    medio = reta3

# indicar a ordem

print(menor, medio, maior)

# fazem uma reta?
if menor + medio > maior:
    print('Elas fazem um triangulo')
else:
    print('Elas não fazem um triangulo')
