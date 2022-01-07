# Preço de uma viagem
from time import sleep

cores = {
    'limpo': '\033[m',
    'verde': '\033[32m',
    'amarelo': '\033[33m'
}

linha_verde = f'{cores["verde"]}-=-' * 11 + f'{cores["limpo"]}'


def analise_preco(km):
    if km <= 200:
        preco = km * 0.5
    else:
        preco = km * 0.45
    return preco


def main():

    print(
        f'{linha_verde}\n{cores["amarelo"]}Preço da viagem...{cores["limpo"]}\n{linha_verde}')

    km = str(input('Digite a distância de sua viagem: ')).strip()
    km = float(km.split()[0])
    print(linha_verde)

    sleep(1)

    print(f'{cores["amarelo"]}ANALISANDO...')
    print(linha_verde)

    sleep(1)

    preco = analise_preco(km)

    print(
        f'Sua viagem vai custar: {cores["amarelo"]}R${preco:.2f}{cores["limpo"]}\n{linha_verde}')


if __name__ == "__main__":
    main()
