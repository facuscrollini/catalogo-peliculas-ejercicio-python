print('*** Excepciones ***')

def dividir(numero, denominador):
    try:
        resultado = numero / denominador
        print(f"El resultado de la división es {resultado}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    finally:
        print('Terminamos de procesar la excepción')
        
        
dividir(10,2)
