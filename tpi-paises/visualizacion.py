from datos import cargar_datos

def mostrar_paises(paises):
    """Muestra países en formato tabular."""
    if not paises:
        print("No se encontraron resultados.")
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
    
    #Población
    mayor_pob = max(paises, key=lambda x: x['poblacion'])
    menor_pob = min(paises, key=lambda x: x['poblacion'])
    total_pob = sum(p['poblacion'] for p in paises)

    #Superficie
    mayor_sup = max(paises, key=lambda x: x['superficie'])
    menor_sup = min(paises, key=lambda x: x['superficie'])
    total_sup = sum(p['superficie'] for p in paises)

    #Promedios
    prom_pob = total_pob / len(paises)
    prom_sup = total_sup / len(paises)

    #Países por continente
    continentes = {}
    for p in paises:
        cont = p['continente']
        continentes[cont] = continentes.get(cont, 0) + 1

    #Mostrar resultados
    print("\n  ESTADÍSTICAS GENERALES")
    print(f"- País con mayor población: {mayor_pob['nombre']} ({mayor_pob['poblacion']:,})")
    print(f"- País con menor población: {menor_pob['nombre']} ({menor_pob['poblacion']:,})")
    print(f"- País con mayor superficie: {mayor_sup['nombre']} ({mayor_sup['superficie']:,} km²)")
    print(f"- País con menor superficie: {menor_sup['nombre']} ({menor_sup['superficie']:,} km²)")
    print(f"- Población promedio: {prom_pob:,.0f}")
    print(f"- Superficie promedio: {prom_sup:,.0f} km²")

    print("\n  Cantidad de países por continente:")
    for cont, cant in continentes.items():
        print(f"  - {cont}: {cant}")