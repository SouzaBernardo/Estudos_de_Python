'''
ler o sexo, aceitar M ou F = digitar novamente
'''


def main():

    # variáveis
    sexos = 'M', 'F'  # para a validação
    flag = True
    while flag == True:
        sexo = str(input('Sexo [M/F]: ')).upper().strip()  # opção escolhida
        # verificar
        if sexo == sexos[0]:
            sexo = 'masculino'
            flag = False
        elif sexo == sexos[1]:
            sexo = 'feminino'
            flag = False
        else:
            # informar erro
            print('Erro: repita o processo...\nO programa só aceita M ou F')
    print(f'Sexo: {sexo}')  # informar resultado


if __name__ == '__main__':
    main()
