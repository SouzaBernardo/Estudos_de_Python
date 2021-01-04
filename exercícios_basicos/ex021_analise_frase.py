# Analisar uma Frase
from unicodedata import normalize

# Pedir frase
frase = str(input('Digite sua frase:')).upper().strip()

# Analisar
# Quantas vezes tem a letra A
quantas_vezes_tem_a = frase.count('A')
# Encontrar a o lugar da primeira letra 
encontrar_a = frase.find('A') + 1 # Adicionamos + 1 porque inicia em 0
# Encontrar a ultima letra A
ultimo_a = frase.rfind('A') + 1 # Não considera os acentos

# Result
print(f'A frase contém {quantas_vezes_tem_a} letra(s) a / as.')
print(f'Nessa frase, a primeira letra A se encontra na posição {encontrar_a}')
print(f'Já a ultima é na posição {ultimo_a}.')
