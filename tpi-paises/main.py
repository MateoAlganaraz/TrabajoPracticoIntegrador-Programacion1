from funciones import *

#Este archivo es el punto de entrada del programa. 
#Gestiona el menú iteractivo y coordina las operaciones de búsqueda, filtrado, ordenamiento y estadísticas
#usando funciones definidas en 'funciones.py'


def mostrar_menu(): #Agregar en funciones.py
    """
    Esta funcón muestra el menú principal de la aplicación en la consola. 
    Ofrece al usuario las opciones disponibles
    """
    print("\n=== GESTIÓN DE DATOS DE PAÍSES ===")
    print("1. Buscar país por nombre")
    print("2. Filtrar por continente")
    print("3. Filtrar por rango de población")
    print("4. Filtrar por rango de superficie")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("0. Salir")

def main():
    """
    Función principal:
    -Carga los datos desde el archivo CSV.
    -Ejecuta un bucle de menú interactivo.
    -Gestiona la entrada del usuario y llama a las funciones adecuadas.
    -Incluye validaciones robustas para evitar errores de entrada.
    """

    try:
        paises = cargar_datos()
        print(f"Datos cargados.")
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return

    #Bucle principal del menú
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                while True:
                    nombre = input("Ingrese nombre (o parte del nombre) del país: ").strip()
                    if nombre:
                        break
                    print("El nombre no puede estar vacío. Por favor ingresa al menos un caracter")
                resultados = buscar_pais_por_nombre(paises, nombre)
                mostrar_paises(resultados)

            case "2":
                while True:
                    continente = input("Ingrese continente (América, Europa, Asia, África, Oceanía): ").strip()
                    if continente:
                        break
                    print("El continente no puede estar vacío. Por favor ingresa un nombre válido.")
                resultados = filtrar_por_continente(paises, continente)
                mostrar_paises(resultados)

            case "3":
                    # Validación robusta con while para rango de población
                    while True:
                        try:
                            min_pob = int(input("Población mínima: "))
                            max_pob = int(input("Población máxima: "))
                            if min_pob > max_pob:
                                print("La población mínima no puede ser mayor que la máxima. Intente nuevamente.")
                                continue
                            break  # Salir del while si todo es válido
                        except ValueError:
                            print("Por favor, ingrese valores numéricos enteros válidos. Intente nuevamente.")
                    
                    resultados = filtrar_por_poblacion(paises, min_pob, max_pob)
                    mostrar_paises(resultados)

            case "4":
                while True:
                    try:
                        min_sup = int(input("Superficie mínima (km²): "))
                        max_sup = int(input("Superficie máxima (km²): "))
                        if min_sup > max_sup: #pedir de nuevo
                            print("La superficie mínima no puede ser mayor que la máxima.")
                            continue
                        break
                    except ValueError:
                        print("Ingrese valores numéricos válidos.")

                resultados = filtrar_por_superficie(paises, min_sup, max_sup)
                mostrar_paises(resultados)
                    

            case "5":
                #Validación para el criterio de ordenamiento (a,b o c)
                while True:
                    print("\nOrdenar por:")
                    print("a) Nombre")
                    print("b) Población")
                    print("c) Superficie")
                    criterio = input("Elija (a/b/c): ").strip().lower()
                    if criterio in ['a', 'b', 'c']:
                        break
                    print("\nOpción inválida. Por favor ingrese 'a', 'b', o 'c'.")

                #Validación para el sentido del orden (a o d)
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
                mostrar_estadisticas(paises)

            case "0":
                print("¡Gracias por usar el sistema!")
                break

            case _:
                print("Opción inválida. Intente nuevamente.")

#Punto de entrada del programa
if __name__ == "__main__":
    main()