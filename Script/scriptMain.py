import random
import os
import difflib
import datetime
import json

# Librerías originales
articulos = ["el", "la", "los", "las", "un", "una", "unos", "unas", "al", "del", "es", "de", "que", "en",
 "quien", "por", "para", "con", "a", "y", "o", "si", "no", "como", "mas", "menos", "muy", "todo", "toda", "todos", "todas",'cual','fue','quienes']

palabrasClaves = ["cambiar", "personaje", "adios", "salir", 'r2d2', 'c-3po', 'yoda', 'chewbacca','c3po']

vocalesTildes = ["á", "é", "í", "ó", "ú"]
vocalesSinTilde = ['a', 'e', 'i', 'o', 'u']

# Globales
newAnsw = []
newQuest = []
esYoda = False
agregoPregunta = False
primeraVez = True
existeArchivoPreguntas = True
existeCarpetaPreguntas = True
existeCarpetaLogs = True
entradaOriginal = ''
entradaModificada = ''
respuestaAgregada = ''
huboCorreccionOrtografica = False



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
            "respuesta_yoda": "“Star Wars: Episode IV: A New Hope” (Una Nueva Esperanza), por orden de estreno la primera fue, en 1977. Pero según el orden cronológico, “Episode I: The Phantom Menace” (La Amenaza Fantasma), en 1999 estrenada fue, sí."
            },
            {
            "preguntas": [
                "En que año se estreno la primera pelicula",
                "En que año se estreno A New Hope",
                "En que año se estreno Una Nueva Esperanza"
            ],
            "respuesta": "La primera película, “A New Hope” (Una nueva esperanza), se estreno en 1977.",
            "respuesta_yoda": "En 1977, la primera película, “A New Hope” (Una nueva esperanza) estrenada fue, mmm."
            },
            {
            "preguntas": [
                "En que año se estreno la segunda pelicula",
                "En que año se estreno The Empire Strikes Back",
                "En que año se estreno El Imperio Contraataca"
            ],
            "respuesta": "La segunda película, “The Empire Strikes Back” (El Imperio Contraataca), se estrenó en 1980.",
            "respuesta_yoda": "En 1980, “The Empire Strikes Back” (El Imperio Contraataca), la segunda película estrenada fue, sí."
            },
            {
            "preguntas": [
                "En que año se estreno la tercera pelicula",
                "En que año se estreno Return of The Jedi",
                "En que año se estreno El Regreso del Jedi"
            ],
            "respuesta": "La tercera película, “Return of The Jedi” (El Retorno del Jedi), se estrenó en 1983.",
            "respuesta_yoda": "“Return of The Jedi” (El Retorno del Jedi), en 1983 lanzada fue, y la tercera película es."
            },
            {
            "preguntas": [
                "En que año se estreno la cuarta pelicula?",
                "En que año se estreno The Phantom Menace?",
                "En que año se estreno La Amenaza Fantasma?"
            ],
            "respuesta": "La cuarta película, “The Phantom Menace”(La Amenaza Fantasma), se estrenó en 1999.",
            "respuesta_yoda": "En 1999, “The Phantom Menace” (La Amenaza Fantasma); la cuarta película estrenada fue, hmmm."
            },
            {
            "preguntas": [
                "En que año se estreno la quinta pelicula",
                "En que año se estreno Attack of the Clones",
                "En que año se estreno El Ataque de los Clones"
            ],
            "respuesta": "La quinta película, “Attack of the Clones” (El Ataque de los Clones), se estrenó en 2002.",
            "respuesta_yoda": "“Attack of the Clones” (El Ataque de los Clones), la quinta, en 2002 estrenada fue."
            },
            {
            "preguntas": [
                "En que año se estreno la sexta pelicula",
                "En que año se estreno Revenge of the Sith",
                "En que año se estreno La Venganza de los Sith"
            ],
            "respuesta": "La sexta película, “Revenge of the Sith”, (La Venganza de los Sith), se estrenó en 2005.",
            "respuesta_yoda": "En 2005, “Revenge of the Sith” (La Venganza de los Sith), estrenada fue, sexta película, es."
            },
            {
            "preguntas": [
                "En que año se estreno The Force Awakens",
                "En que año se estreno El Despertar de la Fuerza",
                "En que año se estreno la septima pelicula"
            ],
            "respuesta": "La séptima película, “The Force Awakens” (El Despertar de la Fuerza), se estrenó en 2015.",
            "respuesta_yoda": "“The Force Awakens” (El Despertar de la Fuerza), séptima película, en 2015 apareció, mmm."
            },
            {
            "preguntas": [
                "En que año se estreno The Last Jedi",
                "En que año se estreno Los Ultimos Jedi",
                "En que año se estreno la octava pelicula"
            ],
            "respuesta": "La octava pelicula, “The Last Jedi” (Los Últimos Jedi), se estrenó en 2017.",
            "respuesta_yoda": "En 2017, “The Last Jedi” (Los Últimos Jedi), la octava película fue, sí."
            },
            {
            "preguntas": [
                "En que año se estreno The Rise of Skywalker",
                "En que año se estreno El Ascenso de Skywalker",
                "En que año se estreno la novena pelicula"
            ],
            "respuesta": "La novena película, “The Rise of Skywalker” (El Ascenso de Skywalker), se estrenó en 2019.",
            "respuesta_yoda": "La novena, “The Rise of Skywalker” (El Ascenso de Skywalker), en 2019 lanzada fue, hmmm."
            },
            {
            "preguntas": [
                "Quien es el creador de Star Wars"
            ],
            "respuesta": "El creador de Star Wars es George Lucas. Es un director, guionista y productor estadounidense que escribió y dirigió la primera película de la saga.",
            "respuesta_yoda": "George Lucas, el creador de Star Wars es. Director, guionista y productor, también, sí."
            },
            {
            "preguntas": [
                "Quien es el padre de Luke Skywalker"
            ],
            "respuesta": "El padre de Luke Skywalker es Anakin Skywalker/Darth Vader.",
            "respuesta_yoda": "Anakin Skywalker, el padre de Luke es. Darth Vader, él también fue."
            }
        ]

        with open("ArchivosDeLectura/preguntas.json", "w", encoding="utf-8") as file:
            json.dump(preguntas, file, ensure_ascii=False, indent=4)
    except Exception as e:
        manejarError(e, "Error al crear el archivo de preguntas")
        return

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
        print("Podés chatear con distintos personajes como R2D2, Chewbacca, Yoda o C-3PO. Cuando desees cambiar de personaje, escribí: cambiar personaje.\n")
        print("En caso que desee salir del programa escriba: salir o adios.")
        personaje = input("Coloque el nombre del personaje con el que desea hablar: ")
        personaje = ortografia(personaje,palabrasClaves)
        personaje = ' '.join(personaje)
        eleccionPersonaje(personaje)
    except KeyboardInterrupt:
        print("\nConversación finalizada, que la fuerza te acompañe.")
    except Exception as e:
        manejarError(e, "Error inesperado en el inicio del programa.")

def agregarInteraccionLogs(entradaOriginal, entradaCorregida, respuesta, personaje):
    """
    Agrega la interacción del usuario y la respuesta del personaje al archivo de log.
    Si el archivo no existe, lo crea y agrega un encabezado.
    Maneja excepciones durante la escritura en el archivo de log.

    Excepciones:
        FileNotFoundError: Si el archivo de log no existe, lo crea.
        Exception: Maneja cualquier otra excepción durante la escritura en el log.
    """
    try:
        with open("Logs/log.txt", "a", encoding="utf-8") as file:
            file.write("\nFecha y hora: " + str(datetime.datetime.now()) + "\n")
            file.write(f"Pregunta: {entradaCorregida}\n")
            if huboCorreccionOrtografica == True:
                file.write(f"Pregunta sin correcion ortografica: {entradaOriginal}\n")
            if agregoPregunta == True  and respuesta == "":
                file.write(f"Respuesta agregada por el usuario: Ocurrio un error, no se agrego una respuesta\n")
                file.write("Porcentaje de acierto con las preguntas: 0%\n")
            elif agregoPregunta == False and respuesta == "":
                file.write(f"Respuesta: El usuario decidio no agregar la pregunta \n")
                file.write("Porcentaje de acierto con las preguntas: 0%\n")
            elif agregoPregunta == True and respuesta != "":
                    file.write(f"Respuesta agregada por el usuario: {respuestaAgregada}\n")
                    file.write("Porcentaje de acierto con las preguntas: 0%\n")
            elif agregoPregunta == False and respuesta != "" and primeraVez == False:
                file.write(f"Respuesta: {respuesta}\n") 
                file.write("Porcentaje de acierto con las preguntas: 100%\n")
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
                agregarInteraccionLogs(entradaOriginal, entradaCorregida, respuesta, personaje)
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
    try:
        global entradaOriginal
        global respuestaAgregada
        global agregoPregunta
        with open("ArchivosDeLectura/preguntas.json", "r", encoding="utf-8") as file:
            preguntas_data = json.load(file)

        if huboCorreccionOrtografica == True:
            entrada = entradaOriginal
        else:
            entrada = entradaModificada
        agrPregunta = input(f"Desea agregar la pregunta '{entrada}' al sistema? (si/no): ").lower().strip("¿?#$%&/()!¡-_[]{.},;:<> ")
        while agrPregunta not in ["si", "no"]:
            agrPregunta = input("No entendí, ¿desea agregar la pregunta al sistema? (si/no): ").lower().strip("¿?#$%&/()!¡ -_[]{.]},;:<>")

        if agrPregunta == 'si':
            answer = input(f"Escriba la respuesta que desea agregar para la pregunta '{entrada}': ")
            respuestaAgregada = answer
            preguntas_data.append({
            "preguntas": [entrada],
            "respuesta": answer,
            "respuesta_yoda": answer
            })
            with open("ArchivosDeLectura/preguntas.json", "w", encoding="utf-8") as file:
                json.dump(preguntas_data, file, ensure_ascii=False, indent=4)
            print("\nPregunta y respuesta agregadas correctamente al sistema.\n")
            agregoPregunta = True
        else:
            agregoPregunta = False
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
            - Omite artículos definidos en la variable global 'articulos'.
        Exceociones:
            En caso de error, maneja la excepción y retorna la entrada original.
        """
        global entradaOriginal
        global entradaModificada
        global huboCorreccionOrtografica
        huboCorreccionOrtografica = False
        entradaOriginal = entrada
        try:
            lista_palabras = entrada.split()
        
            entrada = limpiadorFrases(entrada)
            salida = []
        
            for palabra in entrada:
                palabra = palabra.lower()
                if palabra in articulos:
                    continue
                if palabra in listado:
                    salida.append(palabra)
                    continue
                try:
                    coincidencias = difflib.get_close_matches(palabra, listado, n=3, cutoff=0.5)
                except Exception as e:
                    manejarError(e, "Error en la búsqueda de coincidencias.")
                    continue
                i = 0
                corregida = False
                while i < len(coincidencias) and  i < 3 :
                    if palabra == coincidencias[i]:
                        break
                    print(f"Palabra: {palabra} - ¿Quisiste decir '{coincidencias[i]}'?")
                    respuesta = input("Escriba 'si' para confirmar o 'no' para continuar: ").lower()
                    while respuesta not in ["si", "no"]:
                        respuesta = input(f"No entendí, ¿desea modificar la palabra {palabra} por {coincidencias[i]}? (si/no): ")
                        respuesta = respuesta.lower().strip("¿?#$%&/()!¡ -_[]{}.,;:<>")

                    posicion = lista_palabras.index(palabra)
                    if respuesta == 'si':
                        salida.append(coincidencias[i])
                        lista_palabras[posicion] = coincidencias[i]
                        huboCorreccionOrtografica = True
                        corregida = True
                        break

                    i += 1

                if not corregida:
                    entradaModificada = []

                    salida.append(palabra)
                    
            entradaModificada = ' '.join(lista_palabras) 
            return salida
        except Exception as e:
            manejarError(e, "Error en la corrección ortográfica.")
            return entradaOriginal



def buscarRespuesta(userInput, questGroup, answGroup):
    """
    Busca la mejor respuesta para una entrada de usuario comparando con grupos de preguntas y respuestas.
    Prarametros:
        userInput (str): Entrada del usuario a analizar.
        questGroup (list[list[str]]): Lista de grupos de preguntas, donde cada grupo es una lista de frases relacionadas.
        answGroup (list[list[str]]): Lista de grupos de respuestas, donde cada grupo es una lista de respuestas correspondientes a questGroup.
    Returns:
        str: La mejor respuesta encontrada según la similitud con la entrada del usuario, o un mensaje predeterminado si no se encuentra coincidencia suficiente.
    Notas:
        - Utiliza coincidencia de palabras y densidad de coincidencias para determinar la mejor respuesta.
    Excepciones:
        Si ocurre una excepción, maneja el error y retorna un mensaje predeterminado.
    """
    mejorIndice = -1
    mejorPuntaje = -1
    umbral = 0.8
    
    try:
        userSet = set(userInput)
        for i, preguntas in enumerate(questGroup):
            for pregunta in preguntas:
                palabrasPregunta = set(limpiadorFrases(pregunta))
                coincidencias = userSet.intersection(palabrasPregunta)
                cantidadCoincidencias = len(coincidencias)

                if cantidadCoincidencias == 0:
                    continue

                densidad = cantidadCoincidencias / len(palabrasPregunta)
                puntaje = cantidadCoincidencias * densidad

                if puntaje > mejorPuntaje:
                    mejorPuntaje = puntaje
                    mejorIndice = i

        if mejorPuntaje >= umbral:
            return answGroup[mejorIndice][0]

        return "No tengo respuesta para esa pregunta, lo siento. Vamos a agregar la pregunta al sistema."
    except Exception as e:
        manejarError(e, "Error en la búsqueda de respuesta")
        return "No tengo respuesta para esa pregunta, lo siento. Vamos a agregar la pregunta al sistema."


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
        palabrasClaves = LstPalabrasClaves()
        agregoPregunta = False

        while True:
            if personaje.lower() in ["salir", "adios"]:
                print("Conversación finalizada, que la fuerza te acompañe.")
                break
            personaje = personaje.replace('-','')
            if personaje not in ['yoda', 'chewbacca', 'r2d2', 'c3po'] or personaje == '':
                personaje = input('No entendí, ingrese el personaje nuevamente: ')
                try:
                    personaje = ortografia(personaje,palabrasClaves)
                    personaje = ' '.join(personaje)
                    continue
                except Exception as e:
                    manejarError(e, "Error en la elección del personaje.")
                    continue

            global primeraVez
            if primeraVez == True:
                print(f"\nElegiste hablar con {personaje.upper()}. Puedes hacerle preguntas o cambiar de personaje escribiendo 'cambiar personaje'.")
                print("Escribe 'salir' o 'adios' para finalizar la conversación.\n")

            entrada = input("Tú: ")

            if entrada.lower() in ["salir", "adios"]:
                print("Conversación finalizada, que la fuerza te acompañe.")
                break

            if entrada.lower() in ["cambiar de personaje", "cambiar personaje"]:
                personaje = input('¿Qué personaje desea elegir? ')
                primeraVez = True
                continue

            if entrada.lower() == '':
                primeraVez = False
                print("No entendí, por favor escriba una pregunta.")
                continue

            match personaje.lower():
                case 'r2d2' | 'chewbacca':
                    primeraVez = False
                    frasesr2d2 = ['beep', 'Beep bep', 'Bep beep', 'Bpep', 'Beep beep beeep', 'bep']
                    fraseschewbacca = ['Grrrrowr', 'Hwaaurrgh', 'ghaawwu', 'huagg', 'Rrwaahhggg', 'Grrrruuughhh']
                    if personaje == 'r2d2':
                        print(f"{personaje.upper()}:", random.choice(frasesr2d2))
                    else:
                        print(f"{personaje.upper()}:", random.choice(fraseschewbacca))

                case 'yoda' | 'c3po':
                    primeraVez = False
                    try:
                        entrada = entrada.lower().strip("¿?#$%&/()!¡-_[]}{.,;:<>")
                        entrada = ortografia(entrada,palabrasClaves)
                        if personaje == 'yoda':
                            respuesta = lectorPregunta(entrada, True)
                        else:
                            respuesta = lectorPregunta(entrada, False)
                        if respuesta == "No tengo respuesta para esa pregunta, lo siento. Vamos a agregar la pregunta al sistema.":
                            print(f"{personaje.upper()}:", respuesta)
                            respuesta = ''
                            agregarPregunta()
                            agregarInteraccionLogs(entradaOriginal, entradaModificada, respuestaAgregada, personaje.upper())
                            print(f"{personaje.upper()}: Hazme otra pregunta")
                            """Una vez que se agrega la pregunta, se envia al usuario al inicio del programa para que pueda elegir con que personaje chatear."""
                            return eleccionPersonaje(personaje)
                        if respuesta == None:
                            print(f"{personaje.upper()}: No tengo respuesta para esa pregunta, lo siento. Vamos a agregar la pregunta al sistema.")
                            respuesta = ''
                            agregarPregunta()
                            print(f"{personaje.upper()}: Hazme otra pregunta")
                            return eleccionPersonaje(personaje)
                        print(f"{personaje.upper()}:", respuesta)
                        if huboCorreccionOrtografica == True:
                            correccion = input("Era la respuesta correcta? (si/no): ").lower().strip("¿?#$%&/()!¡-_[]}{.,;:<>")
                            while correccion not in ["si", "no"]:
                                correccion = input("No entendí, ¿era la respuesta correcta? (si/no): ").lower()
                            if correccion == 'no':
                                agregarPregunta()
                                print(f"{personaje.upper()}: Hazme otra pregunta")
                                return eleccionPersonaje(personaje)
                            if correccion == 'si':
                                print(f"{personaje.upper()}: Hazme otra pregunta")
                        agregarInteraccionLogs(entradaOriginal, entradaModificada, respuesta, personaje.upper())
                        respuesta=''
                    except Exception as e:
                        manejarError(e, "Error procesando la pregunta.")
    except Exception as e:
        manejarError(e, "Error en la conversación.")


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
        return manejarError(e, "Error leyendo las preguntas.")


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
            file.write(f"Error: {mensaje}\n")
            file.write(f"Detalles del error: {e}\n")
            file.write("-" * 50 + "\n")
        print(f"Se ha producido un error: {mensaje}. Se ha registrado en el archivo de logs.")
    except Exception as e:
        print(f"Error al guardar el error en el archivo de registro: {e}")
        


# Ejecutar el programa principal
ancho = 70
print("-" * ancho)
print("          BIENVENIDO AL MEJOR ASISTENTE DE STAR WARS          ")
print("-" * ancho)
inicioPrograma()