# Pedir 3 nomes de alunos / grupos e sortear um deles
from random import choice

# Pedir o nome dos alunos
aluno0 = str(input('Primeiro aluno:')) # Primeiro aluno
aluno1 = str(input('Segundo aluno:')) # Segundo aluno
aluno2 = str(input('Terceiro aluno:')) # Terceiro aluno

# Cria lista
lista = [aluno0, aluno1, aluno2]

# Escolher um aluno da lista
sorteado = choice(lista).upper()

# Dizer o sorteado
print(f'O aluno sorteado foi {sorteado}.')
print('__FIM__')
