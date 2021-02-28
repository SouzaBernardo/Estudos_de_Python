# Converter Metros para cm e mm
# Unidades de medida 
    # 1m == 100 cm
    # 1m == 1000mm
print('Vamos converter!')

metro_converter = float(input('\033[33mQuantos metros queres converter?\033[m'))
cm_convertido = metro_converter * 100 # converter para cm  
mm_convertido = metro_converter * 1000 # converter para mm

print(f'Sua metragem foi \033[33m{metro_converter}m\033[m')
print(f'Em cm, converte-se para \033[33m{cm_convertido}cm\033[m')
print(f'Já, em mm é convertido para \033[33m{mm_convertido}mm\033[m')