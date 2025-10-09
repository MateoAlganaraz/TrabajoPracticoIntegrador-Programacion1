from funciones import *

#Función para mostrar el menú de países
def mostrar_menu():
    print("\n=== GESTIÓN DE DATOS DE PAÍSES ===")
    print("1. Buscar país por nombre")
    print("2. Filtrar por continente")
    print("3. Filtrar por rango de población")
    print("4. Filtrar por rango de superficie")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("0. Salir")

#Función principal
def main():
    #Obtenemos la ruta completa del archivo main.py
    import os 
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    archivo = os.path.join(directorio_actual, "paises.csv")
        
    try:
        paises = cargar_datos(archivo)
        print(f"✅ Cargados {len(paises)} países desde '{archivo}'.")
    except Exception as e:
        print(f"❌ Error al cargar el archivo: {e}")
        return

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre = input("Ingrese nombre (o parte del nombre) del país: ").strip()
            resultados = buscar_pais_por_nombre(paises, nombre)
            mostrar_paises(resultados)

        elif opcion == "2":
            continente = input("Ingrese continente (América, Europa, Asia, África, Oceanía): ").strip()
            resultados = filtrar_por_continente(paises, continente)
            mostrar_paises(resultados)

        elif opcion == "3":
            try:
                min_pob = int(input("Población mínima: "))
                max_pob = int(input("Población máxima: "))
                resultados = filtrar_por_poblacion(paises, min_pob, max_pob)
                mostrar_paises(resultados)
            except ValueError:
                print("❌ Ingrese valores numéricos válidos.")

        elif opcion == "4":
            try:
                min_sup = int(input("Superficie mínima (km²): "))
                max_sup = int(input("Superficie máxima (km²): "))
                resultados = filtrar_por_superficie(paises, min_sup, max_sup)
                mostrar_paises(resultados)
            except ValueError:
                print("❌ Ingrese valores numéricos válidos.")

        elif opcion == "5":
            print("Ordenar por:")
            print("a) Nombre")
            print("b) Población")
            print("c) Superficie")
            criterio = input("Elija (a/b/c): ").strip().lower()
            orden = input("¿Ascendente (a) o Descendente (d)? ").strip().lower()
            descendente = orden == "d"
            resultados = ordenar_paises(paises, criterio, descendente)
            mostrar_paises(resultados)

        elif opcion == "6":
            mostrar_estadisticas(paises)

        elif opcion == "0":
            print("👋 ¡Gracias por usar el sistema!")
            break

        else:
            print("❌ Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()