import csv

def cargar_datos(ruta):
    """Carga los datos desde un archivo CSV y los convierte en una lista de diccionarios."""
    paises = []
    try:
        with open(ruta, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for fila in reader:
                # Validar y convertir tipos
                try:
                    fila['poblacion'] = int(fila['poblacion'])
                    fila['superficie'] = int(fila['superficie'])
                    paises.append(fila)
                except (ValueError, KeyError) as e:
                    print(f"⚠️  Advertencia: fila con datos inválidos ignorada: {fila}")
    except FileNotFoundError:
        raise FileNotFoundError(f"Archivo '{ruta}' no encontrado.")
    return paises

def buscar_pais_por_nombre(paises, nombre):
    """Busca países cuyo nombre contenga la cadena dada (insensible a mayúsculas)."""
    nombre = nombre.lower()
    return [p for p in paises if nombre in p['nombre'].lower()]

def filtrar_por_continente(paises, continente):
    """Filtra países por continente (coincidencia exacta, insensible a mayúsculas)."""
    continente = continente.lower()
    return [p for p in paises if p['continente'].lower() == continente]

def filtrar_por_poblacion(paises, min_pob, max_pob):
    """Filtra países dentro de un rango de población."""
    return [p for p in paises if min_pob <= p['poblacion'] <= max_pob]

def filtrar_por_superficie(paises, min_sup, max_sup):
    """Filtra países dentro de un rango de superficie."""
    return [p for p in paises if min_sup <= p['superficie'] <= max_sup]

def ordenar_paises(paises, criterio, descendente=False):
    """Ordena la lista de países según el criterio indicado."""
    claves = {'a': 'nombre', 'b': 'poblacion', 'c': 'superficie'}
    if criterio not in claves:
        print("❌ Criterio de ordenamiento inválido.")
        return paises
    clave = claves[criterio]
    return sorted(paises, key=lambda x: x[clave], reverse=descendente)

def mostrar_paises(paises):
    """Muestra una lista de países en formato tabular."""
    if not paises:
        print("🔍 No se encontraron resultados.")
        return
    print(f"\n{'País':<15} {'Población':<12} {'Superficie (km²)':<15} {'Continente'}")
    print("-" * 60)
    for p in paises:
        print(f"{p['nombre']:<15} {p['poblacion']:<12,} {p['superficie']:<15,} {p['continente']}")

def mostrar_estadisticas(paises):
    """Muestra estadísticas clave del dataset."""
    if not paises:
        print("❌ No hay datos para calcular estadísticas.")
        return

    # País con mayor/menor población
    mayor_pob = max(paises, key=lambda x: x['poblacion'])
    menor_pob = min(paises, key=lambda x: x['poblacion'])

    # Promedios
    total_pob = sum(p['poblacion'] for p in paises)
    total_sup = sum(p['superficie'] for p in paises)
    prom_pob = total_pob / len(paises)
    prom_sup = total_sup / len(paises)

    # Países por continente
    continentes = {}
    for p in paises:
        cont = p['continente']
        continentes[cont] = continentes.get(cont, 0) + 1

    print("\n📊 ESTADÍSTICAS GENERALES")
    print(f"• País con mayor población: {mayor_pob['nombre']} ({mayor_pob['poblacion']:,})")
    print(f"• País con menor población: {menor_pob['nombre']} ({menor_pob['poblacion']:,})")
    print(f"• Población promedio: {prom_pob:,.0f}")
    print(f"• Superficie promedio: {prom_sup:,.0f} km²")
    print("\n🌎 Cantidad de países por continente:")
    for cont, cant in continentes.items():
        print(f"  - {cont}: {cant}")