import csv
import os

def cargar_datos():
    """Carga países desde 'paises.csv'."""
    paises = []
    try:
        directorio = os.path.dirname(os.path.abspath(__file__))
        ruta = os.path.join(directorio, "paises.csv")
        with open(ruta, 'r', encoding='utf-8') as archivo:
            reader = csv.DictReader(archivo)
            filas = list(reader)
            if not filas:
                print("El archivo 'paises.csv' está vacío.")
                return paises
            for fila in filas:
                try:
                    fila['poblacion'] = int(fila['poblacion'])
                    fila['superficie'] = int(fila['superficie'])
                    paises.append(fila)
                except (ValueError, KeyError):
                    print(f"  Advertencia: fila inválida ignorada: {fila}")
    except FileNotFoundError:
        print("Archivo 'paises.csv' no encontrado.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    return paises

def guardar_paises(paises):
    """Guarda la lista completa de países en el archivo 'países.csv'."""
    try:
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        ruta = os.path.join(directorio_actual, "paises.csv")
        with open(ruta, 'w', newline='', encoding='utf-8') as archivo:
            fieldnames = ['nombre', 'poblacion', 'superficie', 'continente']
            escritor = csv.DictWriter(archivo, fieldnames=fieldnames)
            escritor.writeheader()
            escritor.writerows(paises)
    except Exception as e:
        print(f"Error al guardar los datos: {e}")