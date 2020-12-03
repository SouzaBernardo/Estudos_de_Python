import colorama
colorama.init()

nome = str(input('Nome:')).strip().capitalize()
print('Guten morgen!')

if nome == 'Bernardo':
    print('\033[32m QUE NOME LINDO')
elif nome == 'Pedro' or nome == 'João' or nome == 'Paulo':
    print('Nome bem popular no Brasil')
elif nome == 'Lara':
    print('\033[32m A melhor namorada do mundinho')
else:
    print('Que nome normal...')