from funciones import *

def main():
    """Punto de entrada de la aplicación: carga datos y gestiona el menú interactivo."""
    paises = cargar_datos()
    
    #Salir si no hay datos válidos
    if not paises:
        print("\n No se puede iniciar la aplicación: no hay datos válidos en 'paises.csv'.")
        print("Verifique que el archivo exista, no esté vacío y contenga datos correctos.")
        return 
    
    #Bucle principal del menú
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                print("\n---BUSCAR PAÍS---")
                while True:
                    nombre = input("Ingrese nombre (o parte del nombre) del país: ").strip()
                    if nombre:
                        break
                    print("El nombre no puede estar vacío. Por favor ingresa al menos un caracter")
                resultados = buscar_pais_por_nombre(paises, nombre)
                mostrar_paises(resultados)

            case "2":
                print("\n---FILTRAR POR CONTINENTE---")
                while True:
                    continente = input("Ingrese continente (América, Europa, Asia, África, Oceanía): ").strip()
                    if continente:
                        break
                    print("El continente no puede estar vacío. Por favor ingresa un nombre válido.")
                resultados = filtrar_por_continente(paises, continente)
                mostrar_paises(resultados)

            case "3":
                    print("\n---FILTRAR POR POBLACIÓN---")
                    while True:
                        try:
                            min_pob = int(input("Población mínima: "))
                            max_pob = int(input("Población máxima: "))
                            if min_pob > max_pob:
                                print("La población mínima no puede ser mayor que la máxima. Intente nuevamente.")
                                continue
                            break 
                        except ValueError:
                            print("Por favor, ingrese valores numéricos enteros válidos. Intente nuevamente.")
                    
                    resultados = filtrar_por_poblacion(paises, min_pob, max_pob)
                    mostrar_paises(resultados)

            case "4":
                print("\n---FILTRAR POR SUPERFICIE---")
                while True:
                    try:
                        min_sup = int(input("Superficie mínima (km²): "))
                        max_sup = int(input("Superficie máxima (km²): "))
                        if min_sup > max_sup: 
                            print("La superficie mínima no puede ser mayor que la máxima.")
                            continue
                        break
                    except ValueError:
                        print("Ingrese valores numéricos válidos.")

                resultados = filtrar_por_superficie(paises, min_sup, max_sup)
                mostrar_paises(resultados)
                    

            case "5":
                print("\n---ORDENAR PAÍSES---")
                #Seleccionar criterio de ordenamiento
                while True:
                    print("\nOrdenar por:")
                    print("a) Nombre")
                    print("b) Población")
                    print("c) Superficie")
                    criterio = input("Elija (a/b/c): ").strip().lower()
                    if criterio in ['a', 'b', 'c']:
                        break
                    print("\nOpción inválida. Por favor ingrese 'a', 'b', o 'c'.")

                #Seleccionar orden (ascendente/descendente)
                while True:
                    orden = input("¿Ascendente (a) o Descendente (d)? ").strip().lower()
                    if orden in ['a', 'd']:
                        descendente = (orden == "d")
                        break
                    else:
                        print("\nOpción inválida. Por favor, ingrese 'a' (ascendente) o 'd' (descendente).")

                resultados = ordenar_paises(paises, criterio, descendente)
                mostrar_paises(resultados)

            case "6":
                print("\n---MOSTRAR ESTADÍSTICAS---")
                mostrar_estadisticas(paises)

            case "0":
                print("¡Gracias por usar el sistema!")
                break

            case _:
                print("Opción inválida. Intente nuevamente.")

#Punto de entrada del programa
if __name__ == "__main__":
    main()