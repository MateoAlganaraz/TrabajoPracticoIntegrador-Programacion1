from datos import cargar_datos
from menu import mostrar_menu
from busqueda import buscar_pais, filtrar_continente, filtrar_poblacion, filtrar_superficie, ordenar_paises_opcion
from visualizacion import mostrar_estadisticas
from edicion import agregar_pais, editar_pais, eliminar_pais

def main():
    paises = cargar_datos()
    if not paises:
        print("\nNo se puede iniciar la aplicación: no hay datos válidos en 'paises.csv'.")
        print("Verifique que el archivo exista, no esté vacío y contenga datos correctos.")
        return

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                print("\n---BUSCAR PAÍS---")
                buscar_pais(paises)
                print("-" * 60)

            case "2":
                print("\n---FILTRAR POR CONTINENTE---")
                filtrar_continente(paises)
                print("-" * 60)

            case "3":
                print("\n---FILTRAR POR POBLACIÓN---")
                filtrar_poblacion(paises)
                print("-" * 60)

            case "4":
                print("\n---FILTRAR POR SUPERFICIE---")
                filtrar_superficie(paises)
                print("-" * 60)

            case "5":
                print("\n---ORDENAR PAÍSES---")
                ordenar_paises_opcion(paises)
                print("-" * 60)

            case "6":
                print("\n---MOSTRAR ESTADÍSTICAS---")
                mostrar_estadisticas(paises)
                print("-" * 60)

            case "7":
                print("\n---AGREGAR PAÍS---")
                agregar_pais()
                paises = cargar_datos()  # Recargar
                print("-" * 60)

            case "8":
                print("\n---EDITAR PAÍS---")
                editar_pais()
                paises = cargar_datos()  # Recargar
                print("-" * 60)

            case "9":
                print("\n---ELIMINAR PAÍS---")
                eliminar_pais()
                paises = cargar_datos()  # Recargar
                print("-" * 60)

            case "0":
                print("¡Gracias por usar el sistema!")
                break

            case _:
                print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()