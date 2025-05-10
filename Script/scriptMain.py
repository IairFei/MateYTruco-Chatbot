import random

#Librerias originales

articulos = ["el", "la", "los", "las", "un", "una", "unos", "unas", "al", "del", "es", "de","que","en","quien","por","para","con","a","y","o","si","no","como","mas","menos","muy","todo","toda","todos","todas"]

vocalesTildes = ["á", "é", "í", "ó", "ú"]
vocalesSinTilde = ['a','e','i','o','u']

#Globales
#Se declaran variables globales para almacenar las preguntas y respuestas nuevas que se agregan al sistema.

newAnsw =[]
newQuest= [] 
esYoda = False
agregoPregunta = False


def inicioPrograma():
    #Inicia el programa y solicita al usuario el personaje con el que desea interactuar.
    print("Podés chatear con distintos personajes como R2D2, Chewbacca, Yoda o C-3PO. Cuando desees cambiar de personaje, escribí: cambiar personaje: seguido del nombre.\n")
    personaje = input("Coloque el nombre del personaje con el que desea hablar: ")
    eleccionPersonaje(personaje)

def agregarPregunta(userInput):
    #Agrega una pregunta al archivo de preguntas.txt
    with open("ArchivosDeLectura/preguntas.txt", "a", encoding="utf-8") as file:
        agrPregunta = input("Deseea agregar la pregunta '"+ userInput +"' al sistema? (si/no):").lower().strip("¿?#$%&/()!¡ ")
        #Se le pregunta al usuario si desea agregar la pregunta al sistema.
        #Si la respuesta es afirmativa, se le solicita la respuesta y se agrega al archivo preguntas.txt.
        #Si la respuesta es negativa, se le informa al usuario que no se agregará la pregunta."""
        if agrPregunta == 'si':
            global agregoPregunta
            agregoPregunta = True
            userInput = ''.join(userInput)
            file.write("\n")
            file.write(f"\nQ: {userInput}\n")
            answer = input("Escriba la respuesta que desea agregar para la pregunta '" + userInput + "':")
            file.write(f"A: {answer}\n")
            file.write(f"YA: {answer}")

            global newAnsw
            global newQuest
            
            newQuest.append(userInput)
            newAnsw.append(answer)
            
            file.write("\n")
            print("\nPregunta y respuesta agregadas correctamente al sistema.\n")

def buscarRespuesta(userInput, questGroup, answGroup):
    mejorIndice = -1
    mejorPuntaje = -1
    umbral = 0.8
    userSet = set(userInput)  # Evita contar duplicados y mejora velocidad

    for i, preguntas in enumerate(questGroup):
        for pregunta in preguntas:
            palabrasPregunta = set(limpiadorFrases(pregunta))  # También como set

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


def eleccionPersonaje(personaje):
    #Permite al usuario elegir un personaje y mantener una conversación con él.
    while True:

        if personaje.lower() in ["salir", "adios"]:
            #Si el usuario ingresa 'salir' o 'adios', se finaliza la conversación.
            print("Conversación finalizada, que la fuerza te acompañe.")
            break

        if personaje.lower() not in ['yoda', 'chewbacca', 'r2d2', 'c-3po']:
            #Si el personaje ingresado no es válido, se solicita nuevamente al usuario que ingrese un personaje
            personaje = input('No entendí, ingrese el personaje nuevamente: ')
            continue

        entrada = input("Tú: ")

        if entrada.lower() in ["salir", "adios"]:
            #Si el usuario ingresa 'salir' o 'adios', se finaliza la conversación
            print("Conversación finalizada, que la fuerza te acompañe.")
            break

        if entrada.lower() in ["cambiar de personaje", "cambiar personaje"]:
            #Si el usuario desea cambiar de personaje, se solicita el nuevo personaje
            personaje = input('¿Qué personaje desea elegir? ')
            continue
        #Se utiliza un bloque match para determinar el personaje elegido y responder en consecuencia.
        match personaje.lower():
            case 'r2d2' | 'chewbacca':
                #Si el personaje es R2D2 o Chewbacca, se generan frases aleatorias para cada uno.
                #Se utilizan listas de frases predefinidas para cada personaje y se elige una al azar

                frasesr2d2 = ['beep','Beep bep','Bep beep','Bpep','Beep beep beeep','bep']
                fraseschewbacca = ['Grrrrowr','Hwaaurrgh','ghaawwu','huagg','Rrwaahhggg','Grrrruuughhh']
                if personaje == 'r2d2':
                    print(f"{personaje}:", random.choice(frasesr2d2))
                else:
                    print(f"{personaje}:", random.choice(fraseschewbacca))

            case 'yoda' | 'c-3po':
                #Si el personaje es Yoda o C-3PO, se utiliza la función lectorPregunta para obtener una respuesta a la pregunta del usuario.
                #Se le pasa la entrada del usuario y un boooleano para determinar la respuesta adecuada dependiendo de si el usuario.
                #esta hablando con Yoda o C-3PO.
                if personaje == 'yoda':
                    respuesta = lectorPregunta(limpiadorFrases(entrada.lower().strip("¿?#$%&/()!¡")), True)
                else:
                    respuesta = lectorPregunta(limpiadorFrases(entrada.lower().strip("¿?#$%&/()!¡")), False)
                #Se verifica si la respuesta es válida y se imprime en pantalla.
                #Si la respuesta es "No tengo respuesta para esa pregunta, lo siento. Vamos a agregar la pregunta al sistema.
                #Significa que no se encontró una respuesta y se le enviará al usuario a la función agregarPregunta para que pueda agregarla al sistema.    

                if respuesta == "No tengo respuesta para esa pregunta, lo siento. Vamos a agregar la pregunta al sistema.":
                    print(f"{personaje}:", respuesta)
                    agregarPregunta(entrada)
                    print(f"{personaje}: Hazme otra pregunta" )
                    """Una vez que se agrega la pregunta, se envia al usuario al inicio del programa para que pueda elegir con que personaje chatear."""
                    return eleccionPersonaje(personaje)
                print(f"{personaje}:", respuesta)

                    
             
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


def lectorPregunta(userInput, esYoda):
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

    if agregoPregunta == True:
            questGroup.append(newQuest)
            answGroup.append(newAnsw)

    return buscarRespuesta(userInput, questGroup, answGroup)


# --- PROGRAMA PRINCIPAL ---
print("--------------------------------------------------------------")
print("          BIENVENIDO AL MEJOR ASISTENTE DE STAR WARS          ")
print("--------------------------------------------------------------")
print("Se inicio el chat, escriba su pregunta. Si desea finalizar el chat escriba salir o adios.")
inicioPrograma()




