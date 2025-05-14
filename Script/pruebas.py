articulos = ["el", "la", "los", "las", "un", "una", "unos", "unas", "al", "del", "es", "de","que","en","quien","por","para","con","a","y","o","si","no","como","mas","menos","muy","todo","toda","todos","todas"]
pClave = ["cambiar", "personaje", "adios", "salir"]

vocalesTildes = ["á","é","í","ó","ú"]
vocalesSinTilde = ['a','e','i','o','u']

def limpiadorFrases(input):
    palabraLimpia = []
    palabra = ''
    
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


def distancia_levenshtein(a, b):
    if a == b:
        return 0
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)

    fila_anterior = list(range(len(b) + 1))
    for i, c1 in enumerate(a):
        fila_actual = [i + 1]
        for j, c2 in enumerate(b):
            insert = fila_actual[j] + 1
            delete = fila_anterior[j + 1] + 1
            replace = fila_anterior[j] + (c1 != c2)
            fila_actual.append(min(insert, delete, replace))
        fila_anterior = fila_actual

    return fila_anterior[-1]


def ortografia(entrada, listado):
    salida = []
    for palabra in entrada:
        mejorCoincidencia = palabra
        menorDistancia = float('inf')

        for clave in listado:
            dist = distancia_levenshtein(palabra, clave)
            if dist < menorDistancia:
                menorDistancia = dist
                mejorCoincidencia = clave

        if menorDistancia <= max(1, len(palabra) * 0.3): 
            salida.append(mejorCoincidencia)
        else:
            salida.append(palabra)

    return salida


#Prender esYoda y agregarPregunta

def LstPalabrasClaves():
    palabrasClaves = []
    temporal = []
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
    
    return palabrasClaves




def lectorPregunta(userInput): #,esYoda):
    questGroup = []
    answGroup = []

    quest = []
    answ = []
    with open("ArchivosDeLectura/preguntas.txt", "r", encoding="utf-8") as file:
        for lineas in file:
            lineas = lineas.strip()
            if lineas.startswith("Q:"):
                quest.append(lineas[3:].lower().strip("¿?#$%&/()¡!"))
            elif lineas.startswith("A:") : #and esYoda == False:
                answ.append(lineas[3:] )
            elif lineas.startswith("YA:"): #and esYoda == True:
                answ.append(lineas[3:])
            elif lineas == "":# guarda las preguntas y respuestas que se ecuentra antes de un caracter ''
                if quest:
                    questGroup.append(quest)
                    answGroup.append(answ)
                    quest = []
                    answ = []
    #Guarda las preguntas y respuestas que se encuentran al final del documento txt
    questGroup.append(quest)
    answGroup.append(answ)

        #if agregoPregunta == True:
        #   questGroup.append(newQuest)
        #   answGroup.append(newAnsw)
        #   LstPalabrasClaves()

    return buscarRespuesta(userInput, questGroup, answGroup)


def buscarRespuesta(userInput, questGroup, answGroup):
    mejorIndice = -1
    mejorPuntaje = -1
    umbral = 0.80 
    userSet = set(userInput)  # Evita contar duplicados y mejora velocidad

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



while True:
    inputUsuario = input("escribe tu pregunta:")
    if inputUsuario != 'salir':
        inputUsuario = ortografia(limpiadorFrases(inputUsuario),LstPalabrasClaves())
        print(inputUsuario)
        
    else:
        break

