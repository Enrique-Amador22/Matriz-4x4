def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
    return contenido

def comparar_archivos(archivo1, archivo2):
    contenido1 = leer_archivo(archivo1)
    contenido2 = leer_archivo(archivo2)

    if contenido1 == contenido2:
        print("Los archivos son idénticos.")
    else:
        print("Los archivos no son idénticos.")

# Uso del programa
archivo1 = 'MyFile.txt'  # Reemplaza 'archivo1.txt' con el nombre del primer archivo
archivo2 = 'MyFile.txt'  # Reemplaza 'archivo2.txt' con el nombre del segundo archivo

comparar_archivos(archivo1, archivo2)
