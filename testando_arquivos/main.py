def criar_arquivo():

    iniciar = int(input('Número inicial: '))
    final = int(input('Número final: '))

    formato = str(input('Formato do arquivo (com o ponto): ')).strip().lower()

    destino_dado = str(input('Destino dos exercícios (sem o nome do arquivo): ')).strip()

    for i in range(iniciar, final + 1):
        print(i)
        destino_escrever = open(f'{destino_dado}/ex{i}{formato}', 'w' )
        
    destino_escrever.close()
        
def main():
    criar_arquivo()


if __name__ == "__main__":
    main()