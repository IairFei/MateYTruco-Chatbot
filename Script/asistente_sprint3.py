import random
import os
import difflib
import datetime
import json

# Librerías originales
articulos = ["fue","el", "la", "los", "las", "un", "una", "unos", "unas", "al", "del", "es", "de", "que", "en", "por", "para", "con", "a", "y", "o", "si", "no", "como", "mas", "menos", "muy", "todo", "toda", "todos", "todas","quien", "quienes", "cual", "cuales", "donde", "cuando", "porque"]

pClaves = ["cambiar", "personaje", "adios", "salir", 'r2d2','arturito', 'c-3po', 'yoda', 'chewbacca','c3po','preguntas','frecuentes','menu', 'volver']

vocalesTildes = ["á", "é", "í", "ó", "ú"]
vocalesSinTilde = ['a', 'e', 'i', 'o', 'u']

# Control de flujo
primeraVez = True
esYoda = False
agregoPregunta = False
esPregFrecuente = False

# Archivos y carpetas
existeArchivoPreguntas = True
existeCarpetaPreguntas = True
existeCarpetaLogs = True

# Entrada y salida
entradaOriginal = ''
entradaModificada = ''
respuestaAgregada = ''
preguntaEnArchivo = ""
preguntaAgregada = ""

# Datos nuevos
newQuest = []
newAnsw = []

# Corrección ortográfica
huboCorreccionOrtografica = False
cantCorreccionesOrtograficas = 0

# Índice de mejor coincidencia
numMejorIndice = -1
top3MasParecidas = []
porcentajeAcierto = 0



def textoPersonalizado(personaje, mensaje):
    palabras = mensaje.split()
    lineas = []
    linea_actual = ""
    

    for palabra in palabras:
        if len(linea_actual) + len(palabra) + 1 <= 50:
            if linea_actual != '':
                linea_actual += " "
            linea_actual += palabra
        else:   
            lineas.append(linea_actual)
            linea_actual = palabra
    if linea_actual:
        lineas.append(linea_actual)

    ancho = 0
    for linea in lineas:
        if len(linea) > ancho:
            ancho = len(linea)

    espaciadoParaUsuario = 80

    if personaje == "Tú":
        print(" " * (espaciadoParaUsuario - ancho - 4 ) + "╭" + "─" * (ancho + 2) + "╮")
        for linea in lineas:
            print(" " * (espaciadoParaUsuario - ancho - 4 ) + "│ " + linea.ljust(ancho) + " │")
        print(" " * (espaciadoParaUsuario - ancho - 4) + "╰" + "─" * (ancho + 1) + "⋁ ")
        print(" " * espaciadoParaUsuario + personaje)
    else:
        print("  ╭" + "─" * (ancho + 2) + "╮")
        for linea in lineas:
            print("  │ " + linea.ljust(ancho) + " │")
        print("  ⋁ " + "─" * (ancho + 1) + "╯")
        print('', personaje)


def crearArchivoPreguntas():
    """
    Crea el archivo 'ArchivosDeLectura/preguntas.txt' con un conjunto de preguntas y respuestas,
    incluyendo variantes de preguntas y respuestas en estilo convencional y en estilo Yoda.
    Si ocurre un error durante la creación o escritura del archivo, se maneja la
    excepción llamando a la función 'manejarError'.

    Excepciones: Si ocurre un error al crear o escribir en el archivo, la excepción es capturada y gestionada.
    """
    try:
        preguntas = [
            {
            "preguntas": [
                "Cual fue la primera pelicula"
            ],
            "respuesta": "La primera película por orden de estreno fue “Star Wars: Episode IV: A New Hope” (Una Nueva Esperanza), de 1977. Sin embargo, la primera película según el orden cronológico es “Star Wars: Episode I: The Phantom Menace” (La Amenaza Fantasma), de 1999.",
            "respuesta_yoda": "“Star Wars: Episode IV: A New Hope” (Una Nueva Esperanza), por orden de estreno la primera fue, en 1977. Pero según el orden cronológico, “Episode I: The Phantom Menace” (La Amenaza Fantasma), en 1999 estrenada fue, sí.",
            "veces_preguntado": 0
            },
            {
            "preguntas": [
                "En que año se estreno la primera pelicula",
                "En que año se estreno A New Hope",
                "En que año se estreno Una Nueva Esperanza"
            ],
            "respuesta": "La primera película, “A New Hope” (Una nueva esperanza), se estreno en 1977.",
            "respuesta_yoda": "En 1977, la primera película, “A New Hope” (Una nueva esperanza) estrenada fue, mmm.",
            "veces_preguntado": 0
            },
            {
            "preguntas": [
                "En que año se estreno la segunda pelicula",
                "En que año se estreno The Empire Strikes Back",
                "En que año se estreno El Imperio Contraataca"
            ],
            "respuesta": "La segunda película, “The Empire Strikes Back” (El Imperio Contraataca), se estrenó en 1980.",
            "respuesta_yoda": "En 1980, “The Empire Strikes Back” (El Imperio Contraataca), la segunda película estrenada fue, sí.",
            "veces_preguntado": 0
            },
            {
            "preguntas": [
                "En que año se estreno la tercera pelicula",
                "En que año se estreno Return of The Jedi",
                "En que año se estreno El Regreso del Jedi"
            ],
            "respuesta": "La tercera película, “Return of The Jedi” (El Retorno del Jedi), se estrenó en 1983.",
            "respuesta_yoda": "“Return of The Jedi” (El Retorno del Jedi), en 1983 lanzada fue, y la tercera película es.",
            "veces_preguntado": 0
            },
            {
            "preguntas": [
                "En que año se estreno la cuarta pelicula?",
                "En que año se estreno The Phantom Menace?",
                "En que año se estreno La Amenaza Fantasma?"
            ],
            "respuesta": "La cuarta película, “The Phantom Menace”(La Amenaza Fantasma), se estrenó en 1999.",
            "respuesta_yoda": "En 1999, “The Phantom Menace” (La Amenaza Fantasma); la cuarta película estrenada fue, hmmm.",
            "veces_preguntado": 0
            },
            {
            "preguntas": [
                "En que año se estreno la quinta pelicula",
                "En que año se estreno Attack of the Clones",
                "En que año se estreno El Ataque de los Clones"
            ],
            "respuesta": "La quinta película, “Attack of the Clones” (El Ataque de los Clones), se estrenó en 2002.",
            "respuesta_yoda": "“Attack of the Clones” (El Ataque de los Clones), la quinta, en 2002 estrenada fue.",
            "veces_preguntado": 0
            },
            {
            "preguntas": [
                "En que año se estreno la sexta pelicula",
                "En que año se estreno Revenge of the Sith",
                "En que año se estreno La Venganza de los Sith"
            ],
            "respuesta": "La sexta película, “Revenge of the Sith”, (La Venganza de los Sith), se estrenó en 2005.",
            "respuesta_yoda": "En 2005, “Revenge of the Sith” (La Venganza de los Sith), estrenada fue, sexta película, es.",
            "veces_preguntado": 0
            },
            {
            "preguntas": [
                "En que año se estreno The Force Awakens",
                "En que año se estreno El Despertar de la Fuerza",
                "En que año se estreno la septima pelicula"
            ],
            "respuesta": "La séptima película, “The Force Awakens” (El Despertar de la Fuerza), se estrenó en 2015.",
            "respuesta_yoda": "“The Force Awakens” (El Despertar de la Fuerza), séptima película, en 2015 apareció, mmm.",
            "veces_preguntado": 0
            },
            {
            "preguntas": [
                "En que año se estreno The Last Jedi",
                "En que año se estreno Los Ultimos Jedi",
                "En que año se estreno la octava pelicula"
            ],
            "respuesta": "La octava pelicula, “The Last Jedi” (Los Últimos Jedi), se estrenó en 2017.",
            "respuesta_yoda": "En 2017, “The Last Jedi” (Los Últimos Jedi), la octava película fue, sí.",
            "veces_preguntado": 0
            },
            {
            "preguntas": [
                "En que año se estreno The Rise of Skywalker",
                "En que año se estreno El Ascenso de Skywalker",
                "En que año se estreno la novena pelicula"
            ],
            "respuesta": "La novena película, “The Rise of Skywalker” (El Ascenso de Skywalker), se estrenó en 2019.",
            "respuesta_yoda": "La novena, “The Rise of Skywalker” (El Ascenso de Skywalker), en 2019 lanzada fue, hmmm.",
            "veces_preguntado": 0
            },
            {
            "preguntas": [
                "Quien es el creador de Star Wars"
            ],
            "respuesta": "El creador de Star Wars es George Lucas. Es un director, guionista y productor estadounidense que escribió y dirigió la primera película de la saga.",
            "respuesta_yoda": "George Lucas, el creador de Star Wars es. Director, guionista y productor, también, sí.",
            "veces_preguntado": 0
            },
            {
            "preguntas": [
                "Quien es el padre de Luke Skywalker"
            ],
            "respuesta": "El padre de Luke Skywalker es Anakin Skywalker/Darth Vader.",
            "respuesta_yoda": "Anakin Skywalker, el padre de Luke es. Darth Vader, él también fue.",
            "veces_preguntado": 0
            }
        ]

        with open("ArchivosDeLectura/preguntas.json", "w", encoding="utf-8") as file:
            json.dump(preguntas, file, ensure_ascii=False, indent=4)
    except Exception as e:
        manejarError(e, "Error al crear el archivo de preguntas")
        return
def creditosFinales():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print(""" 
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠊⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀
            ⠀⠀⠀⠀⠀⠀⠀⠀⡰⠈⠀⠀⠠⠂⠂⠀⠀⢀⣀⠀⠀⠀⢀⣀⣴⢟⠛⠉     ╭─────────────────────────────-────────────────╮
            ⠀⠀⠀⠀⠀⠀⠀⣾⣧⡠⣂⣤⣬⣲⣶⢷⣾⣛⠙⠳⠀⣤⣿⡿⠃⠂⠀⠀    │ CREDTOS:                                     |
            ⣀⣀⣀⣀⣀⣀⡀⠛⢿⣷⠟⡋⣩⠻⣗⠀⠻⣝⢻⡌⠀⣍⡥⠊⠀⠀⠀⠀   │ Holm Ian                                     |
            ⠈⠑⢝⡻⠿⣿⣿⣿⣾⡟⠘⢋⡉⠞⠒⠒⠋⠈⢲⣿⣿⡛⠁⠀⠀⠀⠀⠀   │ Feigelman Iair                               |
            ⠀⠀⠀⠈⠑⠢⠍⠙⣿⣿⣄⡀⣠⣎⡀⠤⢤⣢⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀    | Cinti Valentino                              |
            ⠀⠀⠀⠀⠀⠀⠀⠀⠙⠙⣿⣿⣿⣿⣿⣿⣛⣿⣿⣿⡅⠀⠀⠀⠀⠀⠀⠀     | Mora Diego                                   |
            ⠀⠀⠀⠀⠀⠀⠀⢀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⢿⣫⢤⢙⢦⠰⣄⡀⠀⠀    | Guzman Kevin                                 |
            ⠀⠀⠀⠀⠀⢠⣼⣿⣿⣿⣳⢻⣿⣿⣿⣿⣷⠾⠿⠋⠖⠄⠀⠙⠎⢷⡀⠀    |/─────────────────────────────────────────────╯ 
            ⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣯⡁⢿⣿⣿⣶⣶⣶⠶⠞⢉⣇⡀⠀⣀⣼⣷⠀
            ⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣧⡾⢉⡛⠿⠢⢌⢀⣾⣿⣿⣿⣿⣿⣿⠀
            ⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡦⡦⢮⠀⢰⡙⡛⠿⣿⣿⣿⠂
            ⠀⠀⠀⠸⣿⠻⣿⣿⣿⣿⣿⣿⣿⣿⠯⢥⠾⠛⠢⣴⡿⡻⣞⢦⡀⠉⠉⠀
            ⠀⠀⠀⠀⠀⠁⠈⠉⠉⠉⠉⠉⠁⠀⠀⠀⠉⠉⠉⠀⠀⠈⠈⠈⠉⠁⠀         
            ⠀⠀""")
def verificarArchivos():
    """
    Verifica la existencia de las carpetas y archivos necesarios para el funcionamiento del programa.
    Si no existen, los crea e inicializa con contenido predeterminado.
    Acciones realizadas:
    - Verifica y crea la carpeta 'ArchivosDeLectura' si no existe.
    - Verifica y crea el archivo 'preguntas.txt' dentro de 'ArchivosDeLectura' si no existe, utilizando la función crearArchivoPreguntas().
    - Verifica y crea la carpeta 'Logs' si no existe.
    - Verifica y crea el archivo 'errorLogs.txt' dentro de 'Logs' si no existe, inicializándolo con un encabezado.
    - Maneja y reporta errores durante la creación de carpetas y archivos.

    Excepciones:
    - Captura y maneja excepciones durante la creación de carpetas y archivos.
    Excepciones: Llama a la función manejarError en caso de error general.
    """
    try:
        # Verificar si la carpeta existe, si no existe, la crea
        if not os.path.exists("ArchivosDeLectura"):
            global existeCarpetaPreguntas
            existeCarpetaPreguntas = False
            try:
                # Crear la carpeta ArchivosDeLectura
                print("Creando carpeta ArchivosDeLectura...")
                os.makedirs("ArchivosDeLectura")
            except Exception as e:
                # Manejar el error si no se puede crear la carpeta
                print(f"Error al crear la carpeta: {e}")
                verificarArchivos()
                return
            print("Carpeta 'ArchivosDeLectura' creada.")
            
            try:
                # Crear el archivo preguntas.txt dentro de la carpeta ArchivosDeLectura
                print("Creando archivo preguntas.json...")
                crearArchivoPreguntas()
            except Exception as e:
                # Manejar el error si no se puede crear el archivo
                print(f"Error al crear el archivo: {e}")
                verificarArchivos()
                return
            print("Archivo 'preguntas.json' creado con preguntas iniciales.")

        # Verificar si el archivo preguntas.txt existe, si no existe, lo crea
        if not os.path.exists("ArchivosDeLectura/preguntas.json"):
            global existeArchivoPreguntas
            existeArchivoPreguntas = False
            try:
                print("Creando archivo preguntas.json...")
                crearArchivoPreguntas()
            except Exception as e:
                print(f"Error al crear el archivo: {e}")
                return
            print("Archivo 'preguntas.json' creado con preguntas iniciales.")
        if not os.path.exists("Logs"):
            global existeCarpetaLogs
            existeCarpetaLogs=False
            try:
                print("Creando carpeta Logs...")
                os.makedirs("Logs")
            except Exception as e:
                print(f"Error al crear la carpeta: {e} ")
            print("Carpeta 'Logs' creada.")  
            try:
                # Crear el archivo errorLogs.txt dentro de la carpeta Logs
                print("Creando archivo errorLogs.txt...")
                with open("Logs/errorLogs.txt", "w", encoding="utf-8") as file:
                    file.write("Registro de errores:\n")
            except Exception as e:
                # Manejar el error si no se puede crear el archivo
                print(f"Error al crear el archivo: {e}")
                verificarArchivos()
                return
            print("Archivo 'errorLogs.txt' creado.")
        try:
            if not os.path.exists("Logs/errorLogs.txt"):
                # Crear el archivo errorLogs.txt dentro de la carpeta Logs
                print("Creando archivo errorLogs.txt...")
                with open("Logs/errorLogs.txt", "w", encoding="utf-8") as file:
                    file.write("Registro de errores:\n")
                print("Archivo 'errorLogs.txt' creado.")
        except Exception as e:
            # Manejar el error si no se puede crear el archivo
            print(f"Error al crear el archivo: {e}")
            verificarArchivos()
            return
        if not os.path.exists("Logs/log.txt"):
            # Crear el archivo log.txt par guardar las interacciones
            print("Creando archivo log.txt...")
            with open("Logs/log.txt", "w", encoding="utf-8") as file:
                file.write("Registro de log:\n")
            print("Archivo 'log.txt' creado.")                
    except Exception as e:
        manejarError(e, "Error al verificar o crear archivos.")
def LstPalabrasClaves():
    palabrasClaves = []
    temporal = []
    try:
        with open("ArchivosDeLectura/preguntas.json", "r", encoding="utf-8") as file:
            preguntas_data = json.load(file)
            for item in preguntas_data:
                for pregunta in item.get("preguntas", []):
                    temporal = limpiadorFrases(pregunta.lower().strip("¿?#$%&/()¡!"))
                    temporal2 = list(set(temporal))
                    for palabra in temporal2:
                        if palabra not in palabrasClaves:
                            palabrasClaves.append(palabra)
        palabrasClaves = list(set(palabrasClaves))
        return palabrasClaves
    except FileNotFoundError:
        verificarArchivos()
        if existeArchivoPreguntas == False:
            print("Error: No se encontró el archivo de preguntas para agregar. Se ha creado uno nuevo con preguntas iniciales.")
        if existeCarpetaPreguntas == False:
            print("Error: No se encontró la carpeta de preguntas para agregar. Se ha creado una nueva junto a un archivo con preguntas iniciales.")
        print("Por favor, vuelva a intentar.")
    except Exception as e:
        manejarError(e, "Error al leer el archivo de preguntas para obtener palabras clave.")
        return palabrasClaves
    
def limpiadorFrases(input):
    """
    Limpia y tokeniza una cadena de entrada eliminando artículos y reemplazando vocales acentuadas.
    Parámetros:
        input (str): Cadena de entrada a limpiar y tokenizar.
    Retorna:
        list: Lista de palabras limpias de la cadena de entrada, excluyendo artículos y con vocales acentuadas reemplazadas.
    Excepciones:
        Si ocurre un error durante el procesamiento, se maneja con manejarError y retorna None.
    Nota:
        Esta función depende de las variables externas 'vocalesTildes', 'vocalesSinTilde', 'articulos' y la función 'manejarError'.
    """
    palabraLimpia = []
    palabra = ''

    try:
        for letras in input:
            if letras in vocalesTildes:
                indice = vocalesTildes.index(letras)
                letras = vocalesSinTilde[indice]
            if letras == " ":
                if palabra:
                    if palabra in articulos:
                        pass
                    else:
                        palabraLimpia.append(palabra)
                palabra = ''
            else:
                palabra += letras

        if palabra:
            if palabra in articulos:
                pass
            else:
                palabraLimpia.append(palabra)

        return palabraLimpia
    except Exception as e:
        manejarError(e, "Error en el limpiador de frases.")
        return
def stem_basico(palabra):
    for sufijo in ['ando', 'iendo', 'cion', 'sion', 'mente', 'ado', 'ido', 'ar', 'er', 'ir', 'os', 'as', 'es','nes', 'les', 'is', 'os']:
        if palabra.endswith(sufijo):
            return palabra[:-len(sufijo)]
    return palabra

def ortografia(entrada, listado):
    """
    Corrige errores ortográficos en una entrada de texto comparando cada palabra con un listado de palabras válidas.
    Parámetros:
        entrada (str): La cadena de texto a corregir.
        listado (list): Lista de palabras válidas para comparar y corregir.
    Retorna:
        list: Lista de palabras corregidas según el listado proporcionado. Si ocurre un error, retorna la entrada original.
    Notas:
        - Utiliza coincidencias aproximadas para sugerir correcciones ortográficas.
        - Solicita confirmación al usuario antes de realizar una corrección.
        - Corrige artículos definidos en la variable global 'articulos'.
    Excepciones:
        En caso de error, maneja la excepción y retorna la entrada original.
    """
    global entradaOriginal
    global entradaModificada
    global huboCorreccionOrtografica
    global cantCorreccionesOrtograficas
    global articulos

    huboCorreccionOrtografica = False
    entradaOriginal = entrada
    cantCorreccionesOrtograficas = 0

    try:
        lista_palabras = entrada.split()
        entrada_limpia = limpiadorFrases(entrada)
        salida = []

        for pal in listado:
            listado_stem = stem_basico(pal.lower()) 
                        

        for palabra in entrada_limpia:
            palabra = palabra.lower()
            palabra_stem = stem_basico(palabra)

            if palabra_stem not in listado_stem:
                try:
                    coincidencias = difflib.get_close_matches(palabra, listado, n=3, cutoff=0.5)
                except Exception as e:
                    manejarError(e, "Error en la búsqueda de coincidencias.")
                    salida.append(palabra)
                    continue

                i = 0
                corregida = False
                mostroLosiento = False
                while i < len(coincidencias) and i < 3:
                    if palabra == coincidencias[i]:
                        break
                    print(f"SYSTEM: ⚠︎ Palabra no encontrada: '{palabra}'")
                    print(f"SYSTEM: ¿Quisiste decir '{coincidencias[i]}'? Escriba 'si' para confirmar o 'no' para continuar:  ", end="")
                    respuesta = input("").lower().strip("¿?#$%&/()!¡-_[]}{.,;:<=")
                    while respuesta not in ["si", "no"]:
                        respuesta = input(f"SYSTEM: No entendí, ¿desea modificar la palabra {palabra} por {coincidencias[i]}? (si/no): ")
                        respuesta = respuesta.lower().strip("¿?#$%&/()!¡-_[]{.],;:<=")
                        print('\033[F\033[K', end='')

                    if respuesta == 'si':
                        print('\033[F\033[K', end='')
                        print('\033[F\033[K', end='')
                        print('\033[F\033[K', end='')
                        print(f"SYSTEM: Se modifico '{palabra}' por '{coincidencias[i]}'")
                        cantCorreccionesOrtograficas += 1
                        palabra_corregida = coincidencias[i]
                        posicion = lista_palabras.index(palabra)
                        lista_palabras[posicion] = palabra_corregida
                        salida.append(palabra_corregida)
                        huboCorreccionOrtografica = True
                        corregida = True
                        break
                    else:
                        print('\033[F\033[K', end='')
                        print('\033[F\033[K', end='')
                        if not mostroLosiento:
                            print("SYSTEM: Lo siento. Probemos con otra palabra:")
                            mostroLosiento = True
                    i += 1
                if not corregida:
                    print('\033[F\033[K', end='')
                    print('SYSTEM: No se modifico ninguna palabra')
                    salida.append(palabra)
            else:
                salida.append(palabra)

        entradaModificada = ' '.join(lista_palabras)
        return salida

    except Exception as e:
        manejarError(e, "Error en la corrección ortográfica.")
        return entradaOriginal


def preguntasFrecuentes():
    global esPregFrecuente
    # Se inicializan las listas para almacenar preguntas y respuestas
    try:
        # Se verifica si el archivo de preguntas existe, si no existe, se crea
        with open("ArchivosDeLectura/preguntas.json", "r", encoding="utf-8") as file:
            preguntas_data = json.load(file)
        # Ordenar las preguntas por 'veces_preguntado' de mayor a menor y tomar las top 3
        # Se crea una lista de tuplas con las preguntas y su cantidad de veces preguntadas
        # Se ordena la lista de preguntas por la cantidad de veces preguntadas
        preguntas_ordenadas = [(item.get("preguntas", []), item.get("veces_preguntado", 0)) for item in preguntas_data]
        def obtener_veces_preguntado(x):
            # Devuelve el numero de veces que se ha preguntado
            return x[1]
        preguntas_ordenadas.sort(key=obtener_veces_preguntado, reverse=True)
        top3 = preguntas_ordenadas[:3]
        print("\nPreguntas frecuentes:")
        for i, pregunta in enumerate(top3):
            #mostrar como string la pregunta
            print(f"{i+1}. {pregunta[0][0]}?")       
        eleccionPregunta = input("¿Desea hacer una de estas preguntas? (si/no): ").lower().strip("¿?#$%&/()!¡-_[]}{.,;:<>")
        while eleccionPregunta not in ["si", "no"]:
            eleccionPregunta = input("No entendí, ¿desea hacer una de estas preguntas? (si/no): ").lower().strip("¿?#$%&/()!¡-_[]}{.,;:<>")
        if eleccionPregunta == 'si':
            try:
                preguntaElegida = int(input("Escriba el numero de la pregunta que desea hacer: "))
                while preguntaElegida > 3 or preguntaElegida < 1:
                    preguntaElegida = int(input("No entendí, escriba el numero de la pregunta que desea hacer: "))
            except ValueError:
                preguntaElegida = int(input("No entendí, escriba el numero de la pregunta que desea hacer: "))
            esPregFrecuente = True
            busquedaTop3(top3, preguntaElegida, esPregFrecuente,esYoda)
            
            input("Presione Enter para continuar...")
        return
    except KeyboardInterrupt:
        # Si el usuario interrumpe la ejecución, se maneja la excepción
        print("\nConversación finalizada, que la fuerza te acompañe.")
        
    # Si el archivo no existe, se verifica y crea
    except FileNotFoundError:
        verificarArchivos()
        if existeArchivoPreguntas == False and existeCarpetaPreguntas == True:
            print("Error: No se encontró el archivo de preguntas para agregar. Se ha creado uno nuevo con preguntas iniciales.")
        if existeCarpetaPreguntas == False and existeArchivoPreguntas == True:
            print("Error: No se encontró la carpeta de preguntas para agregar. Se ha creado una nueva junto a un archivo con preguntas iniciales.")
        print("Por favor, vuelva a intentar.")    
    except Exception as e:
        # Si ocurre un error al leer el archivo, se maneja la excepción
        return manejarError(e, "Error leyendo las preguntas. -- Preguntas frecuentes.")    

def lectorPregunta(userInput, esYoda):
    """
    Lee preguntas y respuestas desde un archivo, procesa la entrada del usuario y retorna una respuesta apropiada.

    Parámetros:
        userInput (str): Entrada del usuario a comparar con las preguntas almacenadas.
        esYoda (bool): Determina si se usan respuestas estilo Yoda ("YA:") o estándar ("A:").

    Retorna:
        str: La respuesta encontrada al comparar la entrada del usuario con las preguntas y respuestas almacenadas.

    Excepciones:
        KeyboardInterrupt: Si el usuario interrumpe la ejecución.
        FileNotFoundError: Si el archivo o carpeta de preguntas no existe.
        Exception: Para cualquier otro error durante la lectura del archivo.
    """
    questGroup = []
    answGroup = []
    quest = []
    answ = []
    # Se inicializan las listas para almacenar preguntas y respuestas
    try:
        # Se verifica si el archivo de preguntas existe, si no existe, se crea
        with open("ArchivosDeLectura/preguntas.json", "r", encoding="utf-8") as file:
            preguntas_data = json.load(file)
            for item in preguntas_data:
                quest = [pregunta.lower().strip("¿?#$%&/()¡!") for pregunta in item.get("preguntas", [])]
                if esYoda:
                    answ = [item.get("respuesta_yoda", "")]
                else:
                    answ = [item.get("respuesta", "")]
                if quest:
                    questGroup.append(quest)
                    answGroup.append(answ)
        if agregoPregunta == True:
            questGroup.append(newQuest)
            answGroup.append(newAnsw)
        return buscarRespuesta(userInput, questGroup, answGroup)
    except KeyboardInterrupt:
        # Si el usuario interrumpe la ejecución, se maneja la excepción
        print("\nConversación finalizada, que la fuerza te acompañe.")
    # Si el archivo no existe, se verifica y crea
    except FileNotFoundError:
        verificarArchivos()
        if existeArchivoPreguntas == False and existeCarpetaPreguntas == True:
            print("Error: No se encontró el archivo de preguntas para agregar. Se ha creado uno nuevo con preguntas iniciales.")
        if existeCarpetaPreguntas == False and existeArchivoPreguntas == True:
            print("Error: No se encontró la carpeta de preguntas para agregar. Se ha creado una nueva junto a un archivo con preguntas iniciales.")
        print("Por favor, vuelva a intentar.")    
    except Exception as e:
        # Si ocurre un error al leer el archivo, se maneja la excepción
        return manejarError(e, "Error leyendo las preguntas. -- Lector de preguntas.")


def inicioPrograma():
    """
    Inicia el programa principal del chatbot, permitiendo al usuario seleccionar un personaje para conversar.
    Verifica la existencia de archivos necesarios, muestra instrucciones, solicita el nombre del personaje,
    corrige la ortografía del nombre ingresado y gestiona la elección del personaje.
    Maneja interrupciones por teclado y otros errores inesperados.

    Excepciones:
    KeyboardInterrupt: Si el usuario interrumpe la ejecución con Ctrl+C.
    Exception: Para cualquier otro error inesperado, delegando el manejo a la función manejarError.
    """
    try:
        verificarArchivos()
        print(" Podés chatear con los siguientes personajes:")
        print(" - R2D o Arturito")
        print(" - Chewbacca")
        print(" - Yoda")
        print(" - C-3PO o C3PO")

        print("\n Comandos útiles:")
        print(" - Para cambiar de personaje: escribir 'cambiar personaje'")
        print(" - Para ver preguntas frecuentes: escribir 'frecuentes' o 'preguntas frecuentes'")
        print(" - Para salir del programa: escribir 'salir' o 'adios'")
        print(" - Para volver al menú principal: escribir 'volver a menu' o 'menu' o 'volver'")
        personaje = input("\nPor favor, escribí el nombre del personaje con el que querés hablar o algun comando: ")
        personaje = ortografia(personaje,pClaves)
        personaje = ' '.join(personaje)
        if personaje == '':
            print("No entendí, por favor escriba el nombre del personaje.")
            return inicioPrograma()
        if personaje.lower() in ["preguntas frecuentes", "frecuentes"]:
            preguntasFrecuentes()
            return inicioPrograma()
        eleccionPersonaje(personaje)
    except KeyboardInterrupt:
        print("\nConversación finalizada, que la fuerza te acompañe.")
    except Exception as e:
        manejarError(e, "Error inesperado en el inicio del programa.")

def agregarInteraccionLogs(entradaOriginal, preguntaEnArchivo, entradaCorregida, respuesta, personaje):
    """
    Agrega la interacción del usuario y la respuesta del personaje al archivo de log.
    Si el archivo no existe, lo crea y agrega un encabezado.
    Maneja excepciones durante la escritura en el archivo de log.

    Excepciones:
        FileNotFoundError: Si el archivo de log no existe, lo crea.
        Exception: Maneja cualquier otra excepción durante la escritura en el log.
    """
    global cantCorreccionesOrtograficas
    
    try:
        global porcentajeAcierto
        with open("Logs/log.txt", "a", encoding="utf-8") as file:
            file.write("\nFecha y hora: " + str(datetime.datetime.now()) + "\n")
            file.write(f"Pregunta hecha por el usuario: {entradaCorregida}\n")
            if huboCorreccionOrtografica == True:
                file.write(f"Pregunta sin correcion ortografica: {entradaOriginal}\n")
                file.write(f"Pregunta en el archivo: {preguntaEnArchivo}\n")
            if agregoPregunta == True  and respuesta == "":
                file.write(f"Pregunta en el archivo: {preguntaEnArchivo}\n")
                file.write(f"Respuesta agregada por el usuario: Ocurrio un error, no se agrego una respuesta\n")
                file.write(f"Porcentaje de acierto con las preguntas: {porcentajeAcierto}%\n")
            elif agregoPregunta == False and respuesta == "":
                file.write(f"Respuesta: El usuario decidio no agregar la pregunta \n")
                file.write(f"Porcentaje de acierto con las preguntas: 0%\n")
            elif agregoPregunta == True and respuesta != "":
                file.write(f"Pregunta agregada por el usuario al archivo: {preguntaAgregada}\n")
                file.write(f"Respuesta agregada por el usuario: {respuestaAgregada}\n")
                file.write(f"Porcentaje de acierto con las preguntas: No se tendra en cuenta el porcentaje ya que es una pregunta nueva agregada por el usuario\n")
            elif agregoPregunta == False and respuesta != "" and primeraVez == False:
                file.write(f"Pregunta en el archivo: {preguntaEnArchivo}\n")
                file.write(f"Respuesta: {respuesta}\n") 
                file.write(f"Porcentaje de acierto con las preguntas: {porcentajeAcierto}%\n")
            else:
                file.write("Error")
            file.write(f"Personaje: {personaje}\n")        
            file.write("\n")
            file.write("----------------------------------------\n")
    except FileNotFoundError:
        with open("Logs/log.txt", "w", encoding="utf-8") as file:
            verificarArchivos()
            with open("Logs/errorLogs.txt", "a", encoding="utf-8") as file:
                file.write("Error: No se encontró el archivo de log. Se ha creado uno nuevo.\n")
                agregarInteraccionLogs(entradaOriginal, preguntaEnArchivo, entradaCorregida, respuesta, personaje)
    except Exception as e:
        manejarError(e, "Error al agregar interacción al log.")
    


def agregarPregunta():
    """
    Agrega una nueva pregunta y su respuesta al archivo de preguntas después de la confirmación del usuario.
    Solicita al usuario confirmar si desea agregar la pregunta actual (`entradaOriginal`) al sistema.
    Si confirma, pide la respuesta, agrega ambas al archivo y actualiza las listas correspondientes.
    Maneja la ausencia del archivo o carpeta intentando crearlos y reintentando la operación.
    Captura y maneja otras excepciones usando el manejador de errores personalizado.
    
    Variables globales:
        entradaOriginal (str): La pregunta a agregar.
        agregoPregunta (bool): Indicador de si se agregó una pregunta.
        newAnsw (list): Lista para almacenar nuevas respuestas.
        newQuest (list): Lista para almacenar nuevas preguntas.
        existeArchivoPreguntas (bool): Indica si existe el archivo de preguntas.
        existeCarpetaPreguntas (bool): Indica si existe la carpeta de preguntas.
        
    Excepciones:
        FileNotFoundError: Si el archivo o carpeta de preguntas no existe, intenta crearlos y reintenta.
        Exception: Maneja cualquier otra excepción usando `manejarError`.
    """
    cont = 0
    try:
        global entradaOriginal
        global respuestaAgregada
        global agregoPregunta
        global preguntaAgregada
        with open("ArchivosDeLectura/preguntas.json", "r", encoding="utf-8") as file:
            preguntas_data = json.load(file)

        if huboCorreccionOrtografica == True:
            entrada = entradaModificada
        else:
            entrada = entradaOriginal
        agrPregunta = input(f"Desea agregar la pregunta '{entrada}' al sistema? (si/no): ").lower().strip("¿?#$%&/()!¡-_[]{.},;:<> ")
        while agrPregunta not in ["si", "no"]:
            agrPregunta = input("No entendí, ¿desea agregar la pregunta al sistema? (si/no): ").lower().strip("¿?#$%&/()!¡ -_[]{.]},;:<>")

        if agrPregunta == 'si':
            preguntaEnArchivo = True
            while preguntaEnArchivo == True:
                ya_existe = False
                cont = 0
                for item in preguntas_data:
                    preguntas = item.get("preguntas", [])
                    while cont < len(preguntas) and ya_existe == False: 
                        if entrada in preguntas[cont].lower().strip("¿?#$%&/()¡!"):
                            ya_existe = True
                            break
                        cont += 1
                    cont = 0
                if ya_existe:
                    print(f"La pregunta '{entrada}' ya existe en el sistema. Debe reformular la pregunta.")
                    entrada = input(f"Escriba la pregunta que desea agregar: ")
                    entrada = entrada.lower().strip("¿?#$%&/()¡! ")
                    while entrada == "":
                        entrada = input("No entendí, escriba la pregunta que desea agregar: ")
                        entrada = entrada.lower().strip("¿?#$%&/()¡! ")
                else:
                    print(f"La pregunta '{entrada}' no existe en el sistema. Puede agregarla.")
                    preguntaEnArchivo = False
            if preguntaEnArchivo == False:
                answer = input(f"Escriba la respuesta que desea agregar para la pregunta '{entrada}': ")
                if answer == "":
                    while answer == "":
                        answer = input(f"No entendí, escriba la respuesta que desea agregar para la pregunta '{entrada}': ")
                        answer = answer.lower().strip("¿?#$%&/()¡! ")
                respuestaAgregada = answer
                preguntas_data.append({
                "preguntas": [entrada],
                "respuesta": answer,
                "respuesta_yoda": answer,
                "veces_preguntado": 1
                })
                with open("ArchivosDeLectura/preguntas.json", "w", encoding="utf-8") as file:
                    json.dump(preguntas_data, file, ensure_ascii=False, indent=4)
                print("\nPregunta y respuesta agregadas correctamente al sistema.\n")
                agregoPregunta = True
                preguntaAgregada = entrada
        else:
            respuestaAgregada=""
            agregoPregunta = False
        return
    except FileNotFoundError:
        verificarArchivos()
        if existeArchivoPreguntas == False:
            print("Error: No se encontró el archivo de preguntas para agregar. Se ha creado uno nuevo con preguntas iniciales.")
        if existeCarpetaPreguntas == False:
            print("Error: No se encontró la carpeta de preguntas para agregar. Se ha creado una nueva junto a un archivo con preguntas iniciales.")
        print("Por favor, vuelva a intentar.")
        agregarPregunta(entradaOriginal)
    except Exception as e:
        manejarError(e, "Error al agregar la pregunta.")

def buscarRespuesta(userInput, questGroup, answGroup):
    """
    Busca la mejor respuesta para una entrada de usuario comparando con grupos de preguntas y respuestas.

    Parametros:
        userInput (str): Entrada del usuario a analizar.
        questGroup (list[list[str]]): Lista de grupos de preguntas, donde cada grupo es una lista de frases relacionadas.
        answGroup (list[list[str]]): Lista de grupos de respuestas, donde cada grupo es una lista de respuestas correspondientes a questGroup.

    Returns:
        str: La mejor respuesta encontrada según la similitud con la entrada del usuario, o un mensaje predeterminado si no se encuentra coincidencia suficiente.
    """
    mejorIndice = -1
    mejorPuntaje = -1
    umbral = 0.8
    global preguntaEnArchivo
    global numMejorIndice
    global top3MasParecidas
    global porcentajeAcierto
    preguntaEnArchivo = ""

    try:
        top3MasParecidas = []
        userSet = set(userInput)
        coincidencias_lista = []

        for i, preguntas in enumerate(questGroup):
            for pregunta in preguntas:
                palabrasPregunta = set(limpiadorFrases(pregunta))
                coincidencias = userSet.intersection(palabrasPregunta)
                cantidadCoincidencias = len(coincidencias)

                if cantidadCoincidencias == 0:
                    continue

                densidad = cantidadCoincidencias / len(palabrasPregunta)
                puntaje = cantidadCoincidencias * densidad

                coincidencias_lista.append((puntaje, i, pregunta))

                if puntaje > mejorPuntaje:
                    mejorPuntaje = puntaje
                    mejorIndice = i
                    numMejorIndice = i
                    porcentajeAcierto = densidad * 100 # PORCENTANJE DE ACIERTO

        usados = set() #Listado para el top 3
        for puntaje, i, pregunta in coincidencias_lista:
            if i not in usados:
                usados.add(i)
                if questGroup[i]:
                    top3MasParecidas.append(questGroup[i][0])
            if len(top3MasParecidas) == 3:
                break

        if mejorPuntaje >= umbral:
            preguntaEnArchivo = questGroup[mejorIndice][0]
            preguntaEnArchivo = preguntaEnArchivo.capitalize() + "?"
            return answGroup[mejorIndice][0]

        return "No tengo respuesta para esa pregunta, lo siento. Vamos a agregar la pregunta al sistema."

    except Exception as e:
        manejarError(e, "Error en la búsqueda de respuesta")
        return "No tengo respuesta para esa pregunta, lo siento. Vamos a agregar la pregunta al sistema."


def busquedaTop3(listaTop3, preguntaElegida, esPregFrecuente, esYoda):
    questGroup = []
    quest = []
    answ = ""
    global entradaModificada

    try:
        with open("ArchivosDeLectura/preguntas.json", "r", encoding="utf-8") as file:
            preguntas_data = json.load(file)

        if esPregFrecuente:
            preguntaElegida -= 1
            quest = listaTop3[preguntaElegida][0][0]
        else:
            quest = listaTop3[preguntaElegida-1]  # Ajuste de índice para evitar out of range

        print(f"\nPregunta elegida: {quest.capitalize()}?")
        questGroup.append(quest.lower())

        for item in preguntas_data:
            preguntas = item.get("preguntas", [])
            for i in range(len(preguntas)):
                if preguntas[i].lower() == questGroup[0]:
                    # Agregar entradaModificada si no está ya presente
                    ya_existe = any(entradaModificada.lower() == p.lower() for p in item["preguntas"])
                    if not ya_existe:
                        item["preguntas"].append(entradaModificada)

                    # Obtener respuesta
                    if esYoda:
                        answ = item.get("respuesta_yoda", "")
                    else:
                        answ = item.get("respuesta", "")

        print(f"\nRespuesta: {answ}")

        # Incrementar contador de uso
        for item in preguntas_data:
            if quest in item.get("preguntas", []):
                item["veces_preguntado"] += 1

        # Guardar JSON actualizado
        with open("ArchivosDeLectura/preguntas.json", "w", encoding="utf-8") as file:
            json.dump(preguntas_data, file, ensure_ascii=False, indent=4)

        return

    except KeyboardInterrupt:
        print("\nConversación finalizada, que la fuerza te acompañe.")

    except FileNotFoundError:
        verificarArchivos()
        print("Se han regenerado los archivos necesarios. Vuelva a intentar.")

    except Exception as e:
        return manejarError(e, "Error leyendo las preguntas. -- busquedaTop3")


def eleccionPersonaje(personaje):
    """
    Permite al usuario elegir un personaje de Star Wars predefinidos para interactuar en una conversación simulada.
    El usuario puede seleccionar entre los personajes 'yoda', 'chewbacca', 'r2d2', 'c-3po'. 
    Durante la conversación, el usuario puede cambiar de personaje, finalizar la conversación o hacer preguntas al personaje seleccionado.
    Dependiendo del personaje, las respuestas pueden ser frases predefinidas o respuestas generadas a partir de la entrada del usuario.
    Si el sistema no tiene respuesta para una pregunta, se le solicita al usuario agregar la pregunta al sistema.
    Parámetros:
        personaje (str): El nombre del personaje con el que el usuario desea interactuar inicialmente.
    Excepciones:
        Maneja errores relacionados con la elección del personaje y el procesamiento de preguntas, mostrando mensajes apropiados al usuario.
    """
    # Se define la función eleccionPersonaje que permite al usuario elegir un personaje para interactuar
    try:
        global agregoPregunta
        global preguntaEnArchivo
        preguntaEnArchivo = ""
        palabrasClaves = LstPalabrasClaves()
        agregoPregunta = False

        while True:
            if personaje.lower() in ["salir", "adios"]:
                print("Conversación finalizada, que la fuerza te acompañe.")
                break
            if personaje.lower() in ["volver a menu", "menu", "volver"]:
                print("Volviendo al menú principal...")
                return inicioPrograma()
            personaje = personaje.replace('-','')
            if personaje not in ['yoda', 'chewbacca', 'r2d2', 'c3po', 'arturito'] or personaje == '':
                personaje = input('No entendí, ingrese el personaje nuevamente: ')
                try:
                    personaje = ortografia(personaje,pClaves)
                    personaje = ' '.join(personaje)
                    continue
                except Exception as e:
                    manejarError(e, "Error en la elección del personaje.")
                    continue
            global primeraVez
            if primeraVez == True:
                print(f"\nElegiste hablar con {personaje.upper()}. Puedes hacerle preguntas o cambiar de personaje escribiendo 'cambiar personaje'.")
                print("Escribe 'salir' o 'adios' para finalizar la conversación.\n")

            print("Tú: ", end="")
            entrada = input()
            print('\033[F\033[K', end='')  #sube una línea y la borra
            textoPersonalizado("Tú", entrada)
            entrada = entrada.lower().strip("¿?#$%&/()!¡-_[]}{.,;:<>=")
            palabrasClaves.extend(pClaves)
            entrada = ortografia(entrada,palabrasClaves)

            
            if entradaModificada in ["salir", "adios"]:
                print("Conversación finalizada, que la fuerza te acompañe.")
                break
            if entradaModificada in ["volver a menu", "menu", "volver"]:
                print("Volviendo al menú principal...")
                return inicioPrograma()
            if entradaModificada in ["cambiar de personaje", "cambiar personaje"]:
                personaje = input('¿Qué personaje desea elegir? ')
                primeraVez = True
                continue

            if entradaModificada == '':
                primeraVez = False
                print("No entendí, por favor escriba una pregunta.")
                continue

            match personaje.lower():
                case 'r2d2' | 'chewbacca' | 'arturito':
                    primeraVez = False
                    frasesr2d2 = ['beep', 'Beep bep', 'Bep beep', 'Bpep', 'Beep beep beeep', 'bep']
                    fraseschewbacca = ['Grrrrowr', 'Hwaaurrgh', 'ghaawwu', 'huagg', 'Rrwaahhggg', 'Grrrruuughhh']
                    if personaje == 'r2d2' or personaje == 'arturito':
                        print(f"{personaje.upper()}:", random.choice(frasesr2d2))
                    else:
                        print(f"{personaje.upper()}:", random.choice(fraseschewbacca))

                case 'yoda' | 'c3po':
                    primeraVez = False
                    try:
                        if personaje == 'yoda':
                            esYoda = True        
                            respuesta = lectorPregunta(entrada, True)
                        else:
                            esYoda = False
                            respuesta = lectorPregunta(entrada, False)

                        if respuesta == "No tengo respuesta para esa pregunta, lo siento. Vamos a agregar la pregunta al sistema.":
                            textoPersonalizado(personaje.upper(), respuesta)
                            respuesta = ''
                            agregarPregunta()
                            agregarInteraccionLogs(entradaOriginal, preguntaEnArchivo, entradaModificada, respuestaAgregada, personaje.upper())
                            textoPersonalizado(personaje.upper(), 'Hazme otra pregunta')
                            """Una vez que se agrega la pregunta, se envia al usuario al inicio del programa para que pueda elegir con que personaje chatear."""
                            return eleccionPersonaje(personaje)
                        if respuesta == None:
                            textoPersonalizado(personaje.upper(), ' No tengo respuesta para esa pregunta, lo siento. Vamos a agregar la pregunta al sistema.')
                            respuesta = ''
                            agregarPregunta()
                            agregarInteraccionLogs(entradaOriginal, preguntaEnArchivo, entradaModificada, respuestaAgregada, personaje.upper())
                            textoPersonalizado(personaje.upper(), 'Hazme otra pregunta')
                            return eleccionPersonaje(personaje)
                        textoPersonalizado(personaje.upper(), respuesta)
                        correcta = input("Era la respuesta correcta? (si/no): ").lower().strip("¿?#$%&/()!¡-_[]}{.,;:<>=")
                        print('\033[F\033[K', end='')
                        while correcta not in ["si", "no"]:
                            correcta = input("No entendí, ¿era la respuesta correcta? (si/no): ").lower()
                        if correcta == 'no':
                            print("\nLas siguientes preguntas son las que más se parecen a la pregunta que hiciste:\n")
                            for i, pregunta in enumerate(top3MasParecidas):
                                if pregunta:
                                    print(f"{i + 1}. ¿{pregunta.capitalize()}?")
                            eleccionPregunta = input("¿Desea hacer una de estas preguntas? (si/no): ").lower().strip("¿?#$%&/()!¡-_[]}{.,;:<>")
                            while eleccionPregunta not in ["si", "no"]:
                                eleccionPregunta = input("No entendí, ¿desea hacer una de estas preguntas? (si/no): ").lower().strip("¿?#$%&/()!¡-_[]}{.,;:<>")
                            if eleccionPregunta == 'si':
                                try:
                                    preguntaElegida = int(input("Escriba el numero de la pregunta que desea hacer: "))
                                    while preguntaElegida > 3 or preguntaElegida < 1:
                                        preguntaElegida = int(input("No entendí, escriba el numero de la pregunta que desea hacer: "))
                                except ValueError:
                                    # Solicitar nuevamente el número de la pregunta hasta que sea válido
                                    while True:
                                        try:
                                            preguntaElegida = int(input("No entendí, escriba el número de la pregunta que desea hacer: "))
                                            if 1 <= preguntaElegida <= 3:
                                                break
                                            else:
                                                print("Por favor, ingrese un número válido entre 1 y 3.")
                                        except ValueError:
                                            print("Por favor, ingrese un número válido entre 1 y 3.")

                                if esYoda:
                                    busquedaTop3(top3MasParecidas[:4], preguntaElegida, esPregFrecuente, True)
                                else:
                                    busquedaTop3(top3MasParecidas[:4], preguntaElegida, esPregFrecuente, False)
                            else:
                                respuesta = agregarPregunta()
                                agregarInteraccionLogs(entradaOriginal, preguntaEnArchivo, entradaModificada, respuesta, personaje.upper())
                            textoPersonalizado(personaje.upper(), 'Hazme otra pregunta')
                            return eleccionPersonaje(personaje)
                        else:
                            sumarVecesPreguntado(numMejorIndice)
                            textoPersonalizado(personaje.upper(), 'Hazme otra pregunta')
                        agregarInteraccionLogs(entradaOriginal, preguntaEnArchivo, entradaModificada, respuesta, personaje.upper())
                        respuesta=''
                        preguntaEnArchivo=''
                    except Exception as e:
                        manejarError(e, "Error procesando la pregunta.")
    except Exception as e:
        manejarError(e, "Error en la conversación.")

def sumarVecesPreguntado(mejorIndice):
    with open("ArchivosDeLectura/preguntas.json", "r", encoding="utf-8") as file:
        preguntas_data = json.load(file)
        preguntas_data[mejorIndice]["veces_preguntado"] += 1
        with open("ArchivosDeLectura/preguntas.json", "w", encoding="utf-8") as file:
            json.dump(preguntas_data, file, ensure_ascii=False, indent=4)
    global numMejorIndice
    numMejorIndice = -1


# Manejo de errores
def manejarError(e, mensaje):
    """
    Maneja errores capturados durante la ejecución del programa, reseteando la entrada original y registrando los detalles del error en un archivo de logs.
    Args:
        e (Exception): La excepción que fue capturada.
        mensaje (str): Un mensaje descriptivo sobre el contexto o la causa del error.
    """
    global entradaOriginal
    entradaOriginal = ''
    
    # Guardar el error en un archivo de registro
    try:
        with open("Logs/errorLogs.txt", "a", encoding="utf-8") as file:
            file.write("\nFecha y hora: " + str(datetime.datetime.now()) + "\n")
            file.write(f"Error: {mensaje}\n")
            file.write(f"Detalles del error: {e}\n")
            file.write("-" * 50 + "\n")
        print(f"Se ha producido un error: {mensaje}. Se ha registrado en el archivo de logs.")
    except FileNotFoundError:
        with open("Logs/errorLogs.txt", "w", encoding="utf-8") as file:
            file.write("Registro de errores:\n")
            file.write(f"Error: {mensaje}\n")
            file.write(f"Detalles del error: {e}\n")
            file.write("-" * 50 + "\n")
        print("Archivo 'errorLogs.txt' creado y error registrado.")
    except Exception as e:
        print(f"Error al guardar el error en el archivo de registro: {e}")
        
# Ejecutar el programa principal
ancho = 70
print("-" * ancho)
print("          BIENVENIDO AL MEJOR ASISTENTE DE STAR WARS          ")
print("-" * ancho)
inicioPrograma()