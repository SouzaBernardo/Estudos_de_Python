# Dizer o primeiro e ultimo nome

# Pdeir nome
nome = str(input('Nome:')).strip().split()

# Identificar o primeiro e ultimo
primeiro_nome = nome[0].capitalize()
ultimo_nome = nome[-1].capitalize()

# Resultado
print(f'O primeiro nome é {primeiro_nome}')
print(f'E, o ultimo nome é {ultimo_nome}')
print('__FIM__')
