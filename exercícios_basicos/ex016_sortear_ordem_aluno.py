# Pedir o nome dos alunos e dizer a ordem
from random import shuffle

aluno0 = str(input('\033[33mPrimeiro aluno:\033[m')).capitalize()
aluno1 = str(input('\033[33mSegundo aluno:\033[m')).capitalize() 
aluno2 = str(input('\033[33mTerceiro aluno:\033[m')).capitalize()
aluno3 = str(input('\033[33mQuarto aluno:\033[m')).capitalize()

lista = [aluno0, aluno1, aluno2, aluno3]

shuffle(lista)

print(f'A ordem do sorteio é \033[33m{lista[0]}, {lista[1]}, {lista[2]}, {lista[3]}\033[m.')
