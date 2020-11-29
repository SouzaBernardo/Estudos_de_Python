# Pedir o nome dos alunos e dizer a ordem
from random import shuffle

# Pedir o nome dos alunos
aluno0 = str(input('Primeiro aluno:')).capitalize() # Primeiro aluno
aluno1 = str(input('Segundo aluno:')).capitalize() # Segundo aluno
aluno2 = str(input('Terceiro aluno:')).capitalize() # Terceiro aluno
aluno3 = str(input('Quarto aluno:')).capitalize() # Quarto aluno

# Cria lista dos alunos
lista = [aluno0, aluno1, aluno2, aluno3]

# Embaralha a lista
shuffle(lista)

# Dizer a ordem
print(f'A ordem do sorteio é {lista[0]}, {lista[1]}, {lista[2]}, {lista[3]}.')
