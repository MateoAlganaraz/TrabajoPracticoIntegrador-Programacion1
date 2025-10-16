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

# Descripción de Archivos
    --funciones.py
    Contiene todas las funciones de lógica del sistema:

    mostrar_menu(): Muestra el menú principal
    cargar_datos(): Lee y valida el archivo CSV
    buscar_pais_por_nombre(): Búsqueda por coincidencia parcial
    filtrar_por_continente(): Filtrado por continente exacto
    filtrar_por_poblacion(): Filtrado por rango de población
    filtrar_por_superficie(): Filtrado por rango de superficie
    ordenar_paises(): Ordenamiento por múltiples criterios
    mostrar_paises(): Visualización tabular de resultados
    mostrar_estadisticas(): Cálculo y muestra de métricas

    --main.py
    Archivo principal que:

    Carga los datos iniciales
    Gestiona el bucle del menú interactivo
    Valida entradas del usuario
    Coordina las llamadas a funciones

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