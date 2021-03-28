# Dizer o primeiro e ultimo nome
nome = str(input('Nome:')).strip().split()
primeiro_nome = nome[0].capitalize()
ultimo_nome = nome[-1].capitalize()

print('\033[32m-=' * 10 + '\033[m')
print(f'O primeiro nome é \033[33m{primeiro_nome}\033[m.')
print(f'E, o ultimo nome é \033[33m{ultimo_nome}\033[m.')
print('\033[32m-=' * 10 + '\033[m')
print('__FIM__')
