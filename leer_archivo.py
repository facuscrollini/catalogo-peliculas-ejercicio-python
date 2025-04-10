print('*** Leer archivo con python ***')

nombre_archivo = 'mi_archivo.txt'
with open(nombre_archivo, 'w') as archivo:
    archivo.write('Hola, soy el archivo.txt\n')
    archivo.write('Hola, soy el archivo.txt pero en su segunda linea\n')

with open(nombre_archivo, 'r') as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea.strip())
        
print('Leyendo el contenido con el método read:')

with open(nombre_archivo, 'r') as archivo:
    print(archivo.read().strip())