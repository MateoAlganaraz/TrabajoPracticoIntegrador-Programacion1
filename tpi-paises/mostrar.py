from datos import cargar_datos

def mostrar_menu():
    """Muestra el menú principal."""
    print("\n=== GESTIÓN DE DATOS DE PAÍSES ===")
    print("1. Buscar país por nombre")
    print("2. Filtrar por continente")
    print("3. Filtrar por rango de población")
    print("4. Filtrar por rango de superficie")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Agregar país")
    print("8. Editar país")
    print("9. Eliminar país")
    print("0. Salir")


def mostrar_paises(paises):
    """Muestra países en formato tabular."""
    if not paises:
        print("  No se encontraron resultados.")
        return
    print(f"\n{'País':<15} {'Población':<12} {'Superficie (km²)':<15} {'Continente'}")
    print("-" * 60)
    for p in paises:
        print(f"{p['nombre']:<15} {p['poblacion']:<12,} {p['superficie']:<15,} {p['continente']}")


def mostrar_estadisticas(paises):
    """Muestra estadísticas del conjunto de países."""
    if not paises:
        print("  No hay datos para calcular estadísticas.")
        return
    mayor_pob = max(paises, key=lambda x: x['poblacion'])
    menor_pob = min(paises, key=lambda x: x['poblacion'])
    total_pob = sum(p['poblacion'] for p in paises)
    total_sup = sum(p['superficie'] for p in paises)
    prom_pob = total_pob / len(paises)
    prom_sup = total_sup / len(paises)
    continentes = {}
    for p in paises:
        cont = p['continente']
        continentes[cont] = continentes.get(cont, 0) + 1
    print("\n  ESTADÍSTICAS GENERALES")
    print(f"- País con mayor población: {mayor_pob['nombre']} ({mayor_pob['poblacion']:,})")
    print(f"- País con menor población: {menor_pob['nombre']} ({menor_pob['poblacion']:,})")
    print(f"- Población promedio: {prom_pob:,.0f}")
    print(f"- Superficie promedio: {prom_sup:,.0f} km²")
    print("\n  Cantidad de países por continente:")
    for cont, cant in continentes.items():
        print(f"  - {cont}: {cant}")