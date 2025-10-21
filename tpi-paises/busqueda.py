from visualizacion import mostrar_paises

def _input_no_vacio(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Este campo no puede estar vacío.")

def buscar_pais(paises):
    nombre = _input_no_vacio("Ingrese nombre (o parte del nombre) del país: ")
    resultados = [p for p in paises if nombre.lower() in p['nombre'].lower()]
    mostrar_paises(resultados)

def filtrar_continente(paises):
    continente = _input_no_vacio("Ingrese continente (América, Europa, Asia, África, Oceanía): ")
    resultados = [p for p in paises if p['continente'].lower() == continente.lower()]
    mostrar_paises(resultados)

def filtrar_poblacion(paises):
    while True:
        try:
            min_pob = int(input("Población mínima: "))
            max_pob = int(input("Población máxima: "))
            if min_pob <= max_pob:
                break
            print("La población mínima no puede ser mayor que la máxima.")
        except ValueError:
            print("Por favor, ingrese valores numéricos enteros válidos.")
    resultados = [p for p in paises if min_pob <= p['poblacion'] <= max_pob]
    mostrar_paises(resultados)

def filtrar_superficie(paises):
    while True:
        try:
            min_sup = int(input("Superficie mínima (km²): "))
            max_sup = int(input("Superficie máxima (km²): "))
            if min_sup <= max_sup:
                break
            print("La superficie mínima no puede ser mayor que la máxima.")
        except ValueError:
            print("Por favor, ingrese valores numéricos enteros válidos.")
    resultados = [p for p in paises if min_sup <= p['superficie'] <= max_sup]
    mostrar_paises(resultados)

def ordenar_paises_opcion(paises):
    while True:
        print("Ordenar por:\na) Nombre\nb) Población\nc) Superficie")
        criterio = input("Elija (a/b/c): ").strip().lower()
        if criterio in ['a', 'b', 'c']:
            break
        print("Opción inválida. Ingrese 'a', 'b' o 'c'.")
    while True:
        orden = input("¿Ascendente (a) o Descendente (d)? ").strip().lower()
        if orden in ['a', 'd']:
            descendente = (orden == 'd')
            break
        print("Opción inválida. Ingrese 'a' o 'd'.")
    claves = {'a': 'nombre', 'b': 'poblacion', 'c': 'superficie'}
    clave = claves[criterio]
    resultados = sorted(paises, key=lambda x: x[clave], reverse=descendente)
    mostrar_paises(resultados)