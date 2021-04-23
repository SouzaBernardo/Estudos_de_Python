def criar_arquivo():
    
    while True:
        iniciar = int(input('\nNúmero inicial: '))
        final = int(input('Número final: '))
        
        # obriga ao inicial ser menor que o final
        if not iniciar > final:
            break
        else:
            print('     \033[31mERRO: REPITA\033[m')

    
    formato = str(input('\nFormato do arquivo (com o ponto): ')).strip().lower()
    destino_dado = str(input('\nDestino dos exercícios (sem o nome do arquivo): ')).strip()

    for i in range(iniciar, final + 1):
        print(i, end=' ')
        destino_escrever = open(f'{destino_dado}/ex{i}{formato}', 'w' )
    
    print('\n')    
    destino_escrever.close()
        
def main():
    criar_arquivo()


if __name__ == "__main__":
    main()