print('*** Anexar información a nuestro archivo ***')

nombre_archivo = 'mi_archivo.txt'

with open(nombre_archivo, 'a') as archivo:
    archivo.write('Anexando informacion ... \n')
    archivo.write('Saliendo de anexar informacion')
    
    
print(f'Se ha anexado información al archivo: {nombre_archivo}')