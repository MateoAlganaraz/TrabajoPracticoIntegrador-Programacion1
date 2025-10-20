from datos import cargar_datos, guardar_paises
from mostrar import mostrar_paises

def _pedir_nombre_no_vacio(mensaje):
    while True:
        nombre = input(mensaje).strip()
        if nombre:
            return nombre
        print("El nombre no puede estar vacío.")

def agregar_pais():
    print("\n--- AGREGAR NUEVO PAÍS ---")
    paises = cargar_datos()
    while True:
        nombre = _pedir_nombre_no_vacio("Nombre del país: ")
        if any(p['nombre'].lower() == nombre.lower() for p in paises):
            print(f"El país '{nombre}' ya está registrado.")
        else:
            break
    while True:
        try:
            poblacion = int(input("Población: "))
            if poblacion >= 0:
                break
            print("La población debe ser no negativa.")
        except ValueError:
            print("Ingrese un número entero válido.")
    while True:
        try:
            superficie = int(input("Superficie (km²): "))
            if superficie >= 0:
                break
            print("La superficie debe ser no negativa.")
        except ValueError:
            print("Ingrese un número entero válido.")
    continente = _pedir_nombre_no_vacio("Continente: ")
    nuevo = {'nombre': nombre, 'poblacion': poblacion, 'superficie': superficie, 'continente': continente}
    paises.append(nuevo)
    guardar_paises(paises)
    print(f"País '{nombre}' agregado correctamente.")

def editar_pais():
    print("\n--- EDITAR PAÍS ---")
    paises = cargar_datos()
    if not paises:
        print("No hay países registrados.")
        return
    while True:
        nombre_buscar = _pedir_nombre_no_vacio("Nombre del país a editar: ")
        pais = next((p for p in paises if p['nombre'].lower() == nombre_buscar.lower()), None)
        if pais:
            break
        print("País no encontrado.")
    print(f"\nEditando: {pais['nombre']}")
    nuevo_nombre = input(f"Nuevo nombre [{pais['nombre']}]: ").strip()
    if nuevo_nombre:
        pais['nombre'] = nuevo_nombre
    for campo, msg in [('poblacion', 'población'), ('superficie', 'superficie (km²)')]:
        while True:
            entrada = input(f"Nueva {msg} [{pais[campo]}]: ").strip()
            if not entrada:
                break
            try:
                valor = int(entrada)
                if valor >= 0:
                    pais[campo] = valor
                    break
                print(f"La {msg} debe ser no negativa.")
            except ValueError:
                print("Ingrese un número entero válido.")
    nuevo_cont = input(f"Nuevo continente [{pais['continente']}]: ").strip()
    if nuevo_cont:
        pais['continente'] = nuevo_cont
    guardar_paises(paises)
    print("País actualizado correctamente.")

def eliminar_pais():
    print("\n--- ELIMINAR PAÍS ---")
    paises = cargar_datos()
    if not paises:
        print("No hay países registrados.")
        return
    while True:
        nombre = _pedir_nombre_no_vacio("Nombre del país a eliminar: ")
        pais = next((p for p in paises if p['nombre'].lower() == nombre.lower()), None)
        if pais:
            confirm = input(f"¿Eliminar '{pais['nombre']}'? (s/n): ").strip().lower()
            if confirm in ['s', 'si', 'sí']:
                paises = [p for p in paises if p['nombre'].lower() != nombre.lower()]
                guardar_paises(paises)
                print(f"País '{pais['nombre']}' eliminado.")
            else:
                print("Eliminación cancelada.")
            return
        print("País no encontrado.")