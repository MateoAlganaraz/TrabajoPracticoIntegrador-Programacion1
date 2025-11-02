# Participantes
    Ignacio Rodriguez: Carpeta digital y video explicativo 
    Mateo Algañaraz: Repositorio y video explicativo
    -COMISIÓN 3

# Gestión de Datos de Países
    Sistema de gestión y análisis de datos geográficos que permite buscar, filtrar, ordenar y visualizar estadísticas de países a partir de un archivo CSV.

# Descripción
    Esta aplicación de consola permite administrar y consultar información sobre países del mundo, incluyendo datos de población, superficie y continente. Ofrece una interfaz interactiva con múltiples opciones de búsqueda y análisis estadístico.

# Características
    -Búsqueda por nombre: Encuentra países por coincidencia parcial (insensible a mayúsculas).
    -Filtrado por continente: Filtra países de América, Europa, Asia, África u Oceanía.
    -Filtrado por población: Establece rangos de población mínima y máxima.
    -Filtrado por superficie: Define rangos de superficie en km².
    -Ordenamiento múltiple: Ordena por nombre, población o superficie (ascendente/descendente).
    -Estadísticas generales: Visualiza métricas globales y distribución continental.
    -Validación de datos: Manejo robusto de errores en entrada de datos.

# Requisitos
    .Python 3.10 o superior (utiliza la sintaxis match-case)
    .Módulos estándar: csv, os (incluidos en Python)

    No se requieren dependencias externas.

# Instrucciones de uso
    -Ubícate en la carpeta del proyecto desde tu terminal.
    -Ejecuta el programa con el siguiente comando: python main.py
    -Sigue el menú interactivo para navegar por las opciones
    -Al realizar operaciones de agregar, editar o eliminar, los cambios se guardan automáticamente en 'paises.csv'

# Descripción de Archivos
    ~ main.py
        Archivo principal que:
        -Carga los datos iniciales.
        -Gestiona el bucle del menú interactivo.
        -Valida entradas del usuario.
        -Coordina las llamadas a funciones.
    ~ datos.py
        Contiene funciones para:
        -Cargar datos desde 'paises.csv'.
    ~ edicion.py
        Gestiona la lógica para:
        -Agregar, editar y eliminar países.
        -Validar entradas del usuario.
    ~ busqueda.py
        Implementa:
        -Búsqueda por nombre.
        -Filtros por continente, población y superficie
        -Ordenamiento de países
    ~ visualizacion.py
        Se encarga de:
        -Mostrar países en formato tabular.
        -Calcular y mostrar estadísticas generales.

# Manejo de Errores
    El sistema incluye validaciones para:

    - Archivo CSV no encontrado
    - Archivo CSV vacío
    - Datos mal formateados (valores no numéricos)
    - Entradas vacías del usuario
    - Valores numéricos inválidos
    - Rangos inválidos (mínimo > máximo)
    - Opciones de menú incorrectas

# Ejemplos de uso
    1. Buscar país por nombre
    Ingrese nombre (o parte del nombre) del país: ar
    --- Resultado: Argentina, Paraguay

    2. Filtrar por continente
    Ingrese continente: Europa
    --- Resultado: España, Francia

    3. Filtrar por población
    Población mínima: 40000000
    Población máxima: 100000000
    --- Resultado: Países del csv con población entre 40 y 100 millones de habitantes

    4. Filtrar por superficie
    Superficie mínima (km²): 500000
    Superficie máxima (km²): 10000000
    --- Resultado: Países con superficie entre 500k y 10 millones de km²

    5. Ordenar países
    Ordenar por:
    a. Nombre
    b. Población
    c. Superficie
    Elija (a/b/c): b
    ¿Ascendente (a) o Descendente (d)? d
    --- Resultado: Países ordenados por población (mayor a menor)

    6. Estadísticas
    ESTADÍSTICAS GENERALES
    - País con mayor población: China (1,439,323,776)
    - País con menor población: Nueva Zelanda (5,084,300)
    - País con mayor superficie: Rusia (17,098,246 km²)
    - País con menor superficie: Mónaco (2 km²)
    - Población promedio: 217,493,956
    - Superficie promedio: 3,291,162 km²

    Cantidad de países por continente:
    - América: 2
    - Europa: 2
    - Asia: 2
    - África: 2
    - Oceanía: 2

# Formato de Salida
Los resultados se muestran en formato tabular:
País            Población    Superficie (km²)  Continente
------------------------------------------------------------
Argentina       45,376,763   2,780,400         América
Brasil          214,326,223  8,515,767         América

# Link del video
https://www.youtube.com/watch?v=whztu1qeKO8