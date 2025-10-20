import csv
import os

def mostrar_menu(): 
    """Muestra el menú principal de la aplicación"""
    print("\n=== GESTIÓN DE DATOS DE PAÍSES ===")
    print("1. Buscar país por nombre")
    print("2. Filtrar por continente")
    print("3. Filtrar por rango de población")
    print("4. Filtrar por rango de superficie")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Agregar país.")
    print("8. Editar país.")
    print("0. Salir")

def cargar_datos(): 
    """Carga países desde 'países.csv' y los convierte en una lista de diccionarios."""
    paises = []
    try:
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        ruta = os.path.join(directorio_actual, "paises.csv")

        with open(ruta,  'r', encoding='utf-8') as archivo:
            reader = csv.DictReader(archivo)

            #Verificar si el archivo tiene filas de datos
            filas = list(reader)
            if not filas:
                print("El archivo 'paises.csv' está vacío (no contiene datos).")
                return paises #retorna lista vacía
            
            for fila in filas:
                try:
                    #Convierte campos numéricos
                    fila['poblacion'] = int(fila['poblacion'])
                    fila['superficie'] = int(fila['superficie'])
                    paises.append(fila)
                except (ValueError, KeyError) as e:
                    print(f"  Advertencia: fila con datos inválidos ignorada: {fila}")

    except FileNotFoundError:
        print(f"Archivo '{ruta}' no encontrado.")
    except Exception as e:
        print(f" Error inesperado al leer el archivo {e}")

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

def buscar_pais_por_nombre(paises, nombre):
    """Busca países cuyo nombre contenga la cadena dada (insensible a mayúsculas)."""
    nombre = nombre.lower()
    return [p for p in paises if nombre in p['nombre'].lower()]


def filtrar_por_continente(paises, continente):
    """Filtra países por continente (coincidencia exacta, insensible a mayúsculas)."""
    continente = continente.lower()
    return [p for p in paises if p['continente'].lower() == continente]


def filtrar_por_poblacion(paises, min_pob, max_pob):
    """Filtra países cuya población esté dentro del rango."""
    return [p for p in paises if min_pob <= p['poblacion'] <= max_pob]


def filtrar_por_superficie(paises, min_sup, max_sup):
    """Filtra países cuya superficie esté dentro del rango."""
    return [p for p in paises if min_sup <= p['superficie'] <= max_sup]


def ordenar_paises(paises, criterio, descendente=False):
    """Ordena la lista de países según el criterio indicado."""
    claves = {'a': 'nombre', 'b': 'poblacion', 'c': 'superficie'}
    if criterio not in claves:
        print("  Criterio de ordenamiento inválido.")
        return paises
    clave = claves[criterio]
    return sorted(paises, key=lambda x: x[clave], reverse=descendente)


def mostrar_paises(paises):
    """Muestra una lista de países en formato tabular."""
    if not paises:
        print("  No se encontraron resultados.")
        return
    print(f"\n{'País':<15} {'Población':<12} {'Superficie (km²)':<15} {'Continente'}")
    print("-" * 60)
    for p in paises:
        print(f"{p['nombre']:<15} {p['poblacion']:<12,} {p['superficie']:<15,} {p['continente']}")


def mostrar_estadisticas(paises):
    """Muestra estadísticas generales del conjunto de países."""
    if not paises:
        print("  No hay datos para calcular estadísticas.")
        return

    # País con mayor/menor población
    mayor_pob = max(paises, key=lambda x: x['poblacion'])
    menor_pob = min(paises, key=lambda x: x['poblacion'])

    # Calculo de promedios
    total_pob = sum(p['poblacion'] for p in paises)
    total_sup = sum(p['superficie'] for p in paises)
    prom_pob = total_pob / len(paises)
    prom_sup = total_sup / len(paises)

    # Países por continente
    continentes = {}
    for p in paises:
        cont = p['continente']
        continentes[cont] = continentes.get(cont, 0) + 1

    #Mostrar resultados
    print("\n  ESTADÍSTICAS GENERALES")
    print(f"- País con mayor población: {mayor_pob['nombre']} ({mayor_pob['poblacion']:,})")
    print(f"- País con menor población: {menor_pob['nombre']} ({menor_pob['poblacion']:,})")
    print(f"- Población promedio: {prom_pob:,.0f}")
    print(f"- Superficie promedio: {prom_sup:,.0f} km²")
    print("\n  Cantidad de países por continente:")
    for cont, cant in continentes.items():
        print(f"  - {cont}: {cant}")

def agregar_pais():
    """Permite al usuario agregar un nuevo país al archivo."""
    #print("\n---AGREGAR NUEVO PAÍS---")

    #Cargar países actuales para verficar duplicados
    paises_existentes = cargar_datos()

    #Nombre
    while True:
        nombre = input("Nombre del país: ").strip()
        if nombre:
            print("El nombre no puede estar vacío.")
            continue

        #Verificar si ya existe
        nombre_duplicado = False
        for p in paises_existentes:
            if p['nombre'].lower() == nombre.lower():
                print(f"El país '{nombre}' ya está registrado. Ingrese un nombre diferente.")
                nombre_duplicado = True
                break

        if not nombre_duplicado:
            break
        
    #Población
    while True:
        try:
            poblacion = int(input("Población: "))
            if poblacion < 0:
                print("La población debe ser un número entero no negativo.")
                continue
            break
        except ValueError:
            print("Ingrese un número entero válido.")

    #Superficie
    while True:
        try:
            superficie = int(input("Superficie (km²): "))
            if superficie < 0:
                print("La superficie debe ser un número entero no negativo.")
                continue
            break
        except ValueError:
            print("Ingrese un número entero válido.")

    #Continente
    while True:
        continente = input("Continente (América, Europa, Asia, África, Oceanía): ").strip()
        if continente:
            break
        print("El continente no puede estar vacío.")

    #Guardar nuevo país
    nuevo_pais = {
        'nombre': nombre,
        'poblacion': poblacion,
        'superficie': superficie,
        'continente': continente
    }
    paises_existentes.append(nuevo_pais)
    guardar_paises(paises_existentes)
    print(f"País '{nombre}' agregado correctamente.")

def editar_pais():
    """Permite editar los datos de un país existente."""
    paises = cargar_datos()
    if not paises:
        print("No hay países registrados. Agregue al menos uno primero.")
        return
    
    #Buscar países por nombre (con validación de existencia)
    while True:
        nombre_buscar = input("\nNombre del país a editar: ").strip()
        if not nombre_buscar:
            print("El nombre no puede estar vacío.")
            continue

        pais_encontrado = None
        for p in paises:
            if p['nombre'].lower() == nombre_buscar.lower():
                pais_encontrado = p
                break

        if pais_encontrado:
            break
        else:
            print("País no encontrado. Intente con un nombre existente.")

    print(f"\nEditando: {pais_encontrado['nombre']}")
    print("Deje en blanco cualquier campo si no desea cambiarlo.")

    #Editar nombre
    nuevo_nombre = input(f"Nuevo nombre [{pais_encontrado['nombre']}]: ").strip()
    if nuevo_nombre:
        pais_encontrado['nombre'] = nuevo_nombre

    #Editar población
    while True:
        entrada = input(f"Nueva población [{pais_encontrado['poblacion']}]: ").strip()
        if entrada == "":
            break
        try:
            nueva_pob = int(entrada)
            if nueva_pob < 0:
                print("La población no puede ser negativa.")
                continue
            pais_encontrado['poblacion'] = nueva_pob
            break
        except ValueError:
            print("Ingrese un número válido.")

    #Editar superficie
    while True:
        entrada = input(f"Nueva superficie (km²) [{pais_encontrado['superficie']}]: ").strip()
        if entrada == "":
            break
        try:
            nueva_sup = int(entrada)
            if nueva_sup < 0:
                print("La superficie no puede ser negativa.")
                continue
            pais_encontrado['superficie'] = nueva_sup
            break
        except ValueError:
            print("Ingrese un número entero válido.")

    #Editar continente
    while True:
        nuevo_cont = input(f"Nuevo continente: [{pais_encontrado['continente']}]: ").strip()
        if nuevo_cont == "":
            break
        if nuevo_cont:
            pais_encontrado['continente'] = nuevo_cont
            break
        else:
            print("El continente no puede estar vacío.")

    #Guardar cambios 
    guardar_paises(paises)
    print(f"País actualizado correctamente.")

def eliminar_pais():
    """Permite eliminar un país existente del archivo"""
    paises = cargar_datos()
    if not paises:
        print("No hay países registrados. Agregue al menos uno primero.")
        return
    
    #Pedir nombre hasta que sea válido y existente
    while True:
        nombre_a_buscar = input("\nNombre del país a eliminar: ").strip()
        if not nombre_a_buscar:
            print("El nombre no puede estar vacío.")
            continue

        #Buscar coincidencia
        pais_encontrado = None
        for p in paises: 
            if p['nombre'].lower() == nombre_a_buscar.lower():
                pais_encontrado = p
                break

        if pais_encontrado:
            #Confirmar eliminación
            confirm = input(f"Está seguro de eliminar '{pais_encontrado['nombre']}'? (s/n): ").strip().lower()
            if confirm in ['s', 'si', 'sí']:
                paises = [p for p in paises if p['nombre'].lower() != nombre_a_buscar.lower()]
                guardar_paises(paises)
                print(f"País '{pais_encontrado['nombre']}' eliminado correctamente.")
            else:
                print("Eliminación cancelada")
            return
        else:
            print("País no encontrado. Intente con un nombre existente.")