articulos = ["el", "la", "los", "las", "un", "una", "unos", "unas", "al", "del", "es", "de","que","en","quien","por","para","con","a","y","o","si","no","como","mas","menos","muy","todo","toda","todos","todas"]
pClave = ["cambiar", "personaje", "adios", "salir"]
import difflib
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




def ortografia(entrada, listado):
    salida = []
    for palabra in entrada:
        coincidencias = difflib.get_close_matches(palabra, listado, n=1, cutoff=0.7)
        if coincidencias:
            salida.append(coincidencias[0])
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




def lectorPregunta(userInput,esYoda):
    questGroup = []
    answGroup = []
    quest = []
    answ = []
    with open("ArchivosDeLectura/preguntas.txt", "r", encoding="utf-8") as file:
        for lineas in file:
            lineas = lineas.strip()
            if lineas.startswith("Q:"):
                quest.append(lineas[3:].lower().strip("¿?#$%&/()¡!"))
            elif lineas.startswith("A:")  and esYoda == False:
                answ.append(lineas[3:] )
            elif lineas.startswith("YA:") and esYoda == True:
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
        print (answGroup[mejorIndice][0])
        return answGroup[mejorIndice][0]

    return "No tengo respuesta para esa pregunta, lo siento. Vamos a agregar la pregunta al sistema."



while True:
    inputUsuario = input("escribe tu pregunta:")
    if inputUsuario != 'salir':
        inputUsuario = ortografia(limpiadorFrases(inputUsuario),LstPalabrasClaves())
        print(inputUsuario)
        respuesta = lectorPregunta(inputUsuario,False)
        print(respuesta)
        
    else:
        break

