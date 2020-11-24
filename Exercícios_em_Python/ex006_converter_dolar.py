# Converter real para dolar

# Valor do dolar -> 5,44

# Pedir valor em R$
print('Vamos converter seu dinheiro?')
din_real = float(input('Quanto queres converter para dolar? R$'))

# Converter
din_dolar = din_real / 5.44 # Converte R$ para US$

# Dizer o resultado
print('Você, com R${:.2f} é equivalente à US${:.2f}.'.format(din_real, din_dolar))
