# Converter real para dolar
# Valor do dolar -> 5,44
print('\033[33mVamos converter seu dinheiro?\033[m')
din_real = float(input('Quanto queres converter para dolar? R$'))
din_dolar = din_real / 5.44 # Converte R$ para US$
print('Você, com \033[33mR${:.2f}\033[m é equivalente à \033[33mUS${:.2f}\033[m.'.format(din_real, din_dolar))
