# Pedir 3 nomes de alunos / grupos e sortear um deles
from random import choice

aluno0 = str(input('\033[33mPrimeiro aluno:\033[m')).strip()
aluno1 = str(input('\033[33mSegundo aluno:\033[m')).strip()
aluno2 = str(input('\033[33mTerceiro aluno:\033[m')).strip()

lista = [aluno0, aluno1, aluno2]
sorteado = choice(lista).upper()

print('-=' * 8)
print(f'O aluno sorteado foi \033[33m{sorteado}\033[m.')
print('-=' * 8)
print('\033[31m__FIM__\033[m')
