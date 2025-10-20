from mostrar import mostrar_paises

def buscar_pais_por_nombre(paises, nombre):
    nombre = nombre.lower()
    return [p for p in paises if nombre in p['nombre'].lower()]

def filtrar_por_continente(paises, continente):
    continente = continente.lower()
    return [p for p in paises if p['continente'].lower() == continente]

def filtrar_por_poblacion(paises, min_pob, max_pob):
    return [p for p in paises if min_pob <= p['poblacion'] <= max_pob]

def filtrar_por_superficie(paises, min_sup, max_sup):
    return [p for p in paises if min_sup <= p['superficie'] <= max_sup]

def ordenar_paises(paises, criterio, descendente=False):
    claves = {'a': 'nombre', 'b': 'poblacion', 'c': 'superficie'}
    if criterio not in claves:
        print("  Criterio inválido.")
        return paises
    clave = claves[criterio]
    return sorted(paises, key=lambda x: x[clave], reverse=descendente)