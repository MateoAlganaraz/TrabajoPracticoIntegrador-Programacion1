# main.py
from datos import cargar_datos
from mostrar import mostrar_menu
from gestion import agregar_pais, editar_pais, eliminar_pais
from buscar_filtrar import (
    buscar_pais_por_nombre,
    filtrar_por_continente,
    filtrar_por_poblacion,
    filtrar_por_superficie,
    ordenar_paises
)
from mostrar import mostrar_paises, mostrar_estadisticas

def buscar_pais(paises):
    print("\n---BUSCAR PAÍS---")
    while True:
        nombre = input("Nombre (o parte): ").strip()
        if nombre:
            break
        print("El nombre no puede estar vacío.")
    resultados = buscar_pais_por_nombre(paises, nombre)
    mostrar_paises(resultados)
    print("-" * 60)

def filtrar_continente(paises):
    print("\n---FILTRAR POR CONTINENTE---")
    while True:
        cont = input("Continente: ").strip()
        if cont:
            break
        print("El continente no puede estar vacío.")
    res = filtrar_por_continente(paises, cont)
    mostrar_paises(res)
    print("-" * 60)

def filtrar_poblacion(paises):
    print("\n---FILTRAR POR POBLACIÓN---")
    while True:
        try:
            min_p = int(input("Población mínima: "))
            max_p = int(input("Población máxima: "))
            if min_p <= max_p:
                break
            print("Mínimo no puede ser mayor que máximo.")
        except ValueError:
            print("Ingrese números enteros válidos.")
    res = filtrar_por_poblacion(paises, min_p, max_p)
    mostrar_paises(res)
    print("-" * 60)

def filtrar_superficie(paises):
    print("\n---FILTRAR POR SUPERFICIE---")
    while True:
        try:
            min_s = int(input("Superficie mínima: "))
            max_s = int(input("Superficie máxima: "))
            if min_s <= max_s:
                break
            print("Mínimo no puede ser mayor que máximo.")
        except ValueError:
            print("Ingrese números enteros válidos.")
    res = filtrar_por_superficie(paises, min_s, max_s)
    mostrar_paises(res)
    print("-" * 60)

def ordenar(paises):
    print("\n---ORDENAR PAÍSES---")
    while True:
        print("Ordenar por:\na) Nombre\nb) Población\nc) Superficie")
        crit = input("Elija (a/b/c): ").strip().lower()
        if crit in ['a','b','c']:
            break
        print("Opción inválida.")
    while True:
        ord_opc = input("¿Ascendente (a) o Descendente (d)? ").strip().lower()
        if ord_opc in ['a','d']:
            desc = ord_opc == 'd'
            break
        print("Ingrese 'a' o 'd'.")
    res = ordenar_paises(paises, crit, desc)
    mostrar_paises(res)
    print("-" * 60)

def main():
    paises = cargar_datos()
    if not paises:
        print("\nNo se puede iniciar: no hay datos válidos en 'paises.csv'.")
        print("Verifique el archivo.")
        return
    while True:
        mostrar_menu()
        op = input("Seleccione una opción: ").strip()
        match op:
            case "1": buscar_pais(paises)
            case "2": filtrar_continente(paises)
            case "3": filtrar_poblacion(paises)
            case "4": filtrar_superficie(paises)
            case "5": ordenar(paises)
            case "6": 
                print("\n---MOSTRAR ESTADÍSTICAS---")
                mostrar_estadisticas(paises)
                print("-" * 60)
            case "7": 
                agregar_pais()
                paises = cargar_datos()
                print("-" * 60)
            case "8": 
                editar_pais()
                paises = cargar_datos()
                print("-" * 60)
            case "9": 
                eliminar_pais()
                paises = cargar_datos()
                print("-" * 60)
            case "0": 
                print("¡Gracias por usar el sistema!")
                break
            case _: 
                print("Opción inválida.")

if __name__ == "__main__":
    main()