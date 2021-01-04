# Converter Metros para cm e mm
print('Vamos converter!')

# Unidades de medida 
    # 1m == 100 cm
    # 1m == 1000mm

# Pedir valor
metro_converter = float(input('Quantos metros queres converter?'))

# Calcular a conversão
cm_convertido = metro_converter * 100 # converter para cm  
mm_convertido = metro_converter * 1000 # converter para mm

# Dizer o resultado
print('Sua metragem foi {}m'.format(metro_converter))
print('Em cm, converte-se para {}cm'.format(cm_convertido))
print('Já, em mm é convertido para {}mm'.format(mm_convertido))