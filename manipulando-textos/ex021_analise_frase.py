# Analisar uma Frase
frase = str(input('Digite sua frase:')).upper().strip()

quantas_vezes_tem_a = frase.count('A')
encontrar_a = frase.find('A') + 1
ultimo_a = frase.rfind('A') + 1 # Problema com acentuação

print('-=' * 28)
print(f'A frase contém \033[33m{quantas_vezes_tem_a}\033[m letra(s) \033[33ma / as\033[m.')
print('-=' * 28)
print(f'Nessa frase, a primeira letra \033[33mA\033[m se encontra na posição \033[33m{encontrar_a}\033[m.')
print(f'Já a \033[33multima\033[m é na posição \033[33m{ultimo_a}\033[m.')
print('-=' * 28)
