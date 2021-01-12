# Quantas palavras tem em um texto
palavra = str(input('\033[33mQual palavra você quer saber a quantidade?\033[m'))
print('\033[31mDIGITE O TEXTO ABAIXO:\033[m')
texto = str(input(''))
quantidade_palavra = texto.count(palavra) 
# Ideia: dizer a posição onde as palavras se encontram
print(f'A palavra \033[33m{palavra}\033[m no seu texto repete \033[33m{quantidade_palavra}\033[m vezes.')