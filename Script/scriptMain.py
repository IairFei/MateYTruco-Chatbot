import random
import os
import difflib

# Librerías originales
articulos = ["el", "la", "los", "las", "un", "una", "unos", "unas", "al", "del", "es", "de", "que", "en",
 "quien", "por", "para", "con", "a", "y", "o", "si", "no", "como", "mas", "menos", "muy", "todo", "toda", "todos", "todas",'cual','fue','quienes']

personajesYsalida = ["cambiar", "personaje", "adios", "salir", 'r2d2', 'c-3po', 'yoda', 'chewbacca','c3po']

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


def crearArchivoPreguntas():
    try:
        with open("ArchivosDeLectura/preguntas.txt", "w", encoding="utf-8") as file:
        # Preguntas iniciales sobre Star Wars
            file.write("Q: Cual fue la primera pelicula\n")
            file.write("A: La primera película por orden de estreno fue “Star Wars: Episode IV: A New Hope” (Una Nueva Esperanza), de 1977. Sin embargo, la primera película según el orden cronológico es “Star Wars: Episode I: The Phantom Menace” (La Amenaza Fantasma), de 1999.\n")
            file.write("YA: “Star Wars: Episode IV: A New Hope” (Una Nueva Esperanza), por orden de estreno la primera fue, en 1977. Pero según el orden cronológico, “Episode I: The Phantom Menace” (La Amenaza Fantasma), en 1999 estrenada fue, sí.\n")
            file.write("\n")    
            file.write("Q: En que año se estreno la primera pelicula\n")
            file.write("Q: En que año se estreno A New Hope\n")
            file.write("Q: En que año se estreno Una Nueva Esperanza\n")
            file.write("A: La primera película, “A New Hope” (Una nueva esperanza), se estreno en 1977.\n")
            file.write("YA: En 1977, la primera película, “A New Hope” (Una nueva esperanza) estrenada fue, mmm.\n")
            file.write("\n")   
            file.write("Q: En que año se estreno la segunda pelicula\n")
            file.write("Q: En que año se estreno The Empire Strikes Back\n")
            file.write("Q: En que año se estreno El Imperio Contraataca\n")
            file.write("A: La segunda película, “The Empire Strikes Back” (El Imperio Contraataca), se estrenó en 1980.\n")
            file.write("YA: En 1980, “The Empire Strikes Back” (El Imperio Contraataca), la segunda película estrenada fue, sí.\n")
            file.write("\n")
            file.write("Q: En que año se estreno la tercera pelicula\n")
            file.write("Q: En que año se estreno Return of The Jedi\n")
            file.write("Q: En que año se estreno El Regreso del Jedi\n")
            file.write("A: La tercera película, “Return of The Jedi” (El Retorno del Jedi), se estrenó en 1983.\n")
            file.write("YA: “Return of The Jedi” (El Retorno del Jedi), en 1983 lanzada fue, y la tercera película es.\n")
            file.write("\n")
            file.write("Q: En que año se estreno la cuarta pelicula?\n")
            file.write("Q: En que año se estreno The Phantom Menace?\n")
            file.write("Q: En que año se estreno La Amenaza Fantasma?\n")
            file.write("A: La cuarta película, “The Phantom Menace”(La Amenaza Fantasma), se estrenó en 1999.\n")
            file.write("YA: En 1999, “The Phantom Menace” (La Amenaza Fantasma); la cuarta película estrenada fue, hmmm.\n")
            file.write("\n")
            file.write("Q: En que año se estreno la quinta pelicula\n")
            file.write("Q: En que año se estreno Attack of the Clones\n")
            file.write("Q: En que año se estreno El Ataque de los Clones\n")
            file.write("A: La quinta película, “Attack of the Clones” (El Ataque de los Clones), se estrenó en 2002.\n")
            file.write("YA: “Attack of the Clones” (El Ataque de los Clones), la quinta, en 2002 estrenada fue.\n")
            file.write("\n")
            file.write("Q: En que año se estreno la sexta pelicula\n")
            file.write("Q: En que año se estreno Revenge of the Sith\n")
            file.write("Q: En que año se estreno La Venganza de los Sith\n")
            file.write("A: La sexta película, “Revenge of the Sith”, (La Venganza de los Sith), se estrenó en 2005.\n")
            file.write("YA: En 2005, “Revenge of the Sith” (La Venganza de los Sith), estrenada fue, sexta película, es.\n")
            file.write("\n")
            file.write("Q: En que año se estreno The Force Awakens\n")
            file.write("Q: En que año se estreno El Despertar de la Fuerza\n")
            file.write("Q: En que año se estreno la septima pelicula\n")
            file.write("A: La séptima película, “The Force Awakens” (El Despertar de la Fuerza), se estrenó en 2015.\n")
            file.write("YA: “The Force Awakens” (El Despertar de la Fuerza), séptima película, en 2015 apareció, mmm.\n")
            file.write("\n")
            file.write("Q: En que año se estreno The Last Jedi\n")
            file.write("Q: En que año se estreno Los Ultimos Jedi\n")
            file.write("Q: En que año se estreno la octava pelicula\n")
            file.write("A: La octava pelicula, “The Last Jedi” (Los Últimos Jedi), se estrenó en 2017.\n")
            file.write("YA: En 2017, “The Last Jedi” (Los Últimos Jedi), la octava película fue, sí.\n")
            file.write("\n")
            file.write("Q: En que año se estreno The Rise of Skywalker\n")
            file.write("Q: En que año se estreno El Ascenso de Skywalker\n")
            file.write("Q: En que año se estreno la novena pelicula\n")
            file.write("A: La novena película, “The Rise of Skywalker” (El Ascenso de Skywalker), se estrenó en 2019.\n")
            file.write("YA: La novena, “The Rise of Skywalker” (El Ascenso de Skywalker), en 2019 lanzada fue, hmmm.\n")
            file.write("\n")
            file.write("Q: Quien es el creador de Star Wars\n")
            file.write("A: El creador de Star Wars es George Lucas. Es un director, guionista y productor estadounidense que escribió y dirigió la primera película de la saga.\n")
            file.write("YA: George Lucas, el creador de Star Wars es. Director, guionista y productor, también, sí.\n")
            file.write("\n")
            file.write("Q: Quien es el padre de Luke Skywalker\n")
            file.write("A: El padre de Luke Skywalker es Anakin Skywalker/Darth Vader.\n")
            file.write("YA: Anakin Skywalker, el padre de Luke es. Darth Vader, él también fue.\n")
            file.write("\n")
    except Exception as e:
        manejarError(e, "Error al crear el archivo de preguntas")
        return

def verificarArchivos():
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
                return
            print("Carpeta 'ArchivosDeLectura' creada.")
            
            try:
                # Crear el archivo preguntas.txt dentro de la carpeta ArchivosDeLectura
                print("Creando archivo preguntas.txt...")
                crearArchivoPreguntas()
            except Exception as e:
                # Manejar el error si no se puede crear el archivo
                print(f"Error al crear el archivo: {e}")
                return
            print("Archivo 'preguntas.txt' creado con preguntas iniciales.")

        # Verificar si el archivo preguntas.txt existe, si no existe, lo crea
        if not os.path.exists("ArchivosDeLectura/preguntas.txt"):
            global existeArchivoPreguntas
            existeArchivoPreguntas = False
            try:
                print("Creando archivo preguntas.txt...")
                crearArchivoPreguntas()
            except Exception as e:
                print(f"Error al crear el archivo: {e}")
                return
            print("Archivo 'preguntas.txt' creado con preguntas iniciales.")
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
                return
            print("Archivo 'errorLogs.txt' creado.")
            if not os.path.exists("Logs/errorLogs.txt"):
                # Crear el archivo errorLogs.txt dentro de la carpeta Logs
                print("Creando archivo errorLogs.txt...")
                with open("Logs/errorLogs.txt", "w", encoding="utf-8") as file:
                    file.write("Registro de errores:\n")
                print("Archivo 'errorLogs.txt' creado.")
    except Exception as e:
        manejarError(e, "Error al verificar o crear archivos")


def inicioPrograma():
    try:
        verificarArchivos()
        print("Podés chatear con distintos personajes como R2D2, Chewbacca, Yoda o C-3PO. Cuando desees cambiar de personaje, escribí: cambiar personaje.\n")
        print("En caso que desee salir del programa escriba: salir o adios.")
        personaje = input("Coloque el nombre del personaje con el que desea hablar: ")
        personaje = ortografia(personaje,personajesYsalida)
        personaje = ' '.join(personaje)
        eleccionPersonaje(personaje)
    except KeyboardInterrupt:
        print("\nConversación finalizada, que la fuerza te acompañe.")
    except Exception as e:
        manejarError(e, "Error inesperado en el inicio del programa")


def agregarPregunta():
    try:
        global entradaOriginal
        with open("ArchivosDeLectura/preguntas.txt", "a", encoding="utf-8") as file:
            agrPregunta = input(f"Desea agregar la pregunta '{entradaOriginal}' al sistema? (si/no): ").lower().strip("¿?#$%&/()!¡-_[]{}.,;:<> ")
            while agrPregunta not in ["si", "no"]:
                agrPregunta = input("No entendí, ¿desea agregar la pregunta al sistema? (si/no): ").lower().strip("¿?#$%&/()!¡ -_[]{}.,;:<>")

            if agrPregunta == 'si':
                global agregoPregunta, newAnsw, newQuest
                agregoPregunta = True
                file.write(f"\nQ: {entradaOriginal}\n")
                answer = input(f"Escriba la respuesta que desea agregar para la pregunta '{entradaOriginal}': ")
                file.write(f"A: {answer}\n")
                file.write(f"YA: {answer}\n")

                newQuest.append(entradaOriginal)
                newAnsw.append(answer)
                file.write("\n")
                print("\nPregunta y respuesta agregadas correctamente al sistema.\n")
    except FileNotFoundError:
        verificarArchivos()
        if existeArchivoPreguntas == False:
            print("Error: No se encontró el archivo de preguntas para agregar. Se ha creado uno nuevo con preguntas iniciales.")
        if existeCarpetaPreguntas == False:
            print("Error: No se encontró la carpeta de preguntas para agregar. Se ha creado una nueva junto a un archivo con preguntas iniciales.")
        print("Por favor, vuelva a intentar.")
        agregarPregunta(entradaOriginal)
    except Exception as e:
        manejarError(e, "Error al agregar la pregunta")

def LstPalabrasClaves():
    palabrasClaves = []
    temporal = []
    try:
        with open("ArchivosDeLectura/preguntas.txt", "r", encoding="utf-8") as file:
            for lineas in file:
                lineas = lineas.strip()
                if lineas.startswith("Q:"):
                    temporal = limpiadorFrases(lineas[3:].lower().strip("¿?#$%&/()¡!"))
                    temporal2 = list(set(temporal))

                    for palabra in temporal2:
                        if palabra not in palabrasClaves:
                            palabrasClaves.append(palabra)

        palabrasClaves = list(set(palabrasClaves))
        palabrasClaves.extend(personajesYsalida)
        return palabrasClaves
    except FileNotFoundError:
        verificarArchivos()
        if existeArchivoPreguntas == False:
            print("Error: No se encontró el archivo de preguntas para agregar. Se ha creado uno nuevo con preguntas iniciales.")
        if existeCarpetaPreguntas == False:
            print("Error: No se encontró la carpeta de preguntas para agregar. Se ha creado una nueva junto a un archivo con preguntas iniciales.")
        print("Por favor, vuelva a intentar.")
    except Exception as e:
        manejarError(e, "Error al leer el archivo de preguntas para obtener palabras clave")
        return palabrasClaves


def ortografia(entrada, listado):
        global entradaOriginal
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
                    coincidencias = difflib.get_close_matches(palabra, listado, n=2, cutoff=0.5)
                except Exception as e:
                    manejarError(e, "Error en la búsqueda de coincidencias")
                    continue
                i = 0
                corregida = False
                while i < len(coincidencias) and  i < 2 :
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

                        corregida = True
                        break

                    i += 1

                if not corregida:
                    entradaOriginal = []

                    salida.append(palabra)
                    
            entradaOriginal = ' '.join(lista_palabras)
            return salida
        except Exception as e:
            manejarError(e, "Error en la corrección ortográfica")
            return entradaOriginal



def buscarRespuesta(userInput, questGroup, answGroup):
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
    # Se define la función eleccionPersonaje que permite al usuario elegir un personaje para interactuar
    try:
        palabrasClaves = LstPalabrasClaves()
        
        while True:
            if personaje.lower() in ["salir", "adios"]:
                print("Conversación finalizada, que la fuerza te acompañe.")
                break

            if personaje.lower() not in ['yoda', 'chewbacca', 'r2d2', 'c-3po', 'c3po'] or personaje == '':
                personaje = input('No entendí, ingrese el personaje nuevamente: ')
                try:
                    personaje = ortografia(personaje,palabrasClaves)
                    personaje = ' '.join(personaje)
                    continue
                except Exception as e:
                    manejarError(e, "Error en la elección del personaje")
                    continue

            global primeraVez
            if primeraVez == True:
                print(f"\nElegiste hablar con {personaje}. Puedes hacerle preguntas o cambiar de personaje escribiendo 'cambiar personaje'.")
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
                        print(f"{personaje}:", random.choice(frasesr2d2))
                    else:
                        print(f"{personaje}:", random.choice(fraseschewbacca))

                case 'yoda' | 'c-3po' | 'c3po':
                    primeraVez = False
                    try:
                        entrada = entrada.lower().strip("¿?#$%&/()!¡-_[]}{.,;:<>")
                        print(entrada)

                        entrada = ortografia(entrada,palabrasClaves)
                        if entrada[0] in ["salir", "adios"]:
                                print("Conversación finalizada, que la fuerza te acompañe.")
                                break
                        if personaje == 'yoda':
                            respuesta = lectorPregunta(entrada, True)
                        else:
                            respuesta = lectorPregunta(entrada, False)
                        
                        if respuesta == "No tengo respuesta para esa pregunta, lo siento. Vamos a agregar la pregunta al sistema.":
                            print(f"{personaje}:", respuesta)
                            agregarPregunta()
                            print(f"{personaje}: Hazme otra pregunta")
                            """Una vez que se agrega la pregunta, se envia al usuario al inicio del programa para que pueda elegir con que personaje chatear."""
                            return eleccionPersonaje(personaje)
                        if respuesta == None:
                            print(f"{personaje}: No tengo respuesta para esa pregunta, lo siento. Vamos a agregar la pregunta al sistema.")
                            agregarPregunta()
                            print(f"{personaje}: Hazme otra pregunta")
                            return eleccionPersonaje(personaje)
                        print(f"{personaje}:", respuesta)
                    except Exception as e:
                        manejarError(e, "Error procesando la pregunta")
    except Exception as e:
        manejarError(e, "Error en la conversación")


def limpiadorFrases(input):
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
        manejarError(e, "Error en el limpiador de frases")
        return


def lectorPregunta(userInput, esYoda):
    questGroup = []
    answGroup = []
    quest = []
    answ = []
    # Se inicializan las listas para almacenar preguntas y respuestas
    try:
        # Se verifica si el archivo de preguntas existe, si no existe, se crea
        with open("ArchivosDeLectura/preguntas.txt", "r", encoding="utf-8") as file:
            for lineas in file:
                lineas = lineas.strip()
                if lineas.startswith("Q:"):
                    quest.append(lineas[3:].lower().strip("¿?#$%&/()¡!"))
                elif lineas.startswith("A:")  and esYoda == False:
                    answ.append(lineas[3:])
                elif lineas.startswith("YA:") and esYoda == True:
                    answ.append(lineas[3:])
                elif lineas == "":# guarda las preguntas y respuestas que se ecuentra antes de un caracter ''
                    if quest:
                        # Se agrega la pregunta y respuesta a las listas
                        questGroup.append(quest)
                        answGroup.append(answ)
                        quest = []
                        answ = []
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
        return manejarError(e, "Error leyendo las preguntas")


# Manejo de errores
def manejarError(e, mensaje):
    global entradaOriginal
    entradaOriginal = ''
    
    # Guardar el error en un archivo de registro
    try:
        with open("Logs/errorLogs.txt", "a", encoding="utf-8") as file:
            file.write(f"Error: {mensaje}\n")
            file.write(f"Detalles del error: {e}\n")
            file.write("-" * 50 + "\n")
    except Exception as e:
        print(f"Error al guardar el error en el archivo de registro: {e}")


# Ejecutar el programa principal
ancho = 70
print("-" * ancho)
print("          BIENVENIDO AL MEJOR ASISTENTE DE STAR WARS          ")
print("-" * ancho)
inicioPrograma()