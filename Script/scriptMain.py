import random

#Librerias originales
articulos = ["el", "la", "los", "las", "un", "una", "unos", "unas", "al", "del", "es", "de","que","en"]
vocalesTildes = ["á", "é", "í", "ó", "ú"]
vocalesSinTilde = ['a','e','i','o','u']

#Globales
newAnsw =[]
newQuest= [] 
esYoda = False
agregoPregunta = False


def inicioPrograma():
    print("Podés chatear con distintos personajes como R2D2, Chewbacca, Yoda o C-3PO. Cuando desees cambiar de personaje, escribí: cambiar personaje: seguido del nombre.\n")
    personaje = input("Coloque el nombre del personaje con el que desea hablar: ")
    eleccionPersonaje(personaje)

def agregarPregunta(userInput):
    """Agrega una pregunta al archivo de preguntas.txt."""
    with open("ArchivosDeLectura/preguntas.txt", "a", encoding="utf-8") as file:
        agrPregunta = input("Deseea agregar la pregunta '"+ userInput +"' al sistema? (si/no):").lower().strip("¿?#$%&/()!¡ ")
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
            print("\nPregunta y respuesta agregadas correctamente.")

def buscarRespuesta(userInput, questGroup, answGroup):
    coincidenciaMax = 0
    cantCoincidencias = (len(userInput) + 1) // 2
    mejorIndice = 0

    for i in range(len(questGroup)):
        coincidenciasActuales = 0
        for pregunta in questGroup[i]:
            palabrasPregunta = limpiadorFrases(pregunta)
            for palabra in userInput:
                if palabra in palabrasPregunta:
                    coincidenciasActuales += 1
                    
        if coincidenciasActuales > coincidenciaMax:
            coincidenciaMax = coincidenciasActuales
            mejorIndice = i

    if mejorIndice != 0 and coincidenciaMax >= cantCoincidencias:
        return answGroup[mejorIndice][0]
    
    return "No tengo respuesta para esa pregunta, lo siento. Vamos a agregar la pregunta al sistema."


def eleccionPersonaje(personaje):    
    while True:
        if personaje.lower() in ["salir", "adios"]:
            print("Conversación finalizada, que la fuerza te acompañe.")
            break

        if personaje.lower() not in ['yoda', 'chewbacca', 'r2d2', 'c-3po']:
            personaje = input('No entendí, ingrese el personaje nuevamente: ')
            continue

        entrada = input("Tú: ")

        if entrada.lower() in ["salir", "adios"]:
            print("Conversación finalizada, que la fuerza te acompañe.")
            break

        if entrada.lower() in ["cambiar de personaje", "cambiar personaje"]:
            personaje = input('¿Qué personaje desea elegir? ')
            continue

        match personaje.lower():
            case 'r2d2' | 'chewbacca':
                frasesr2d2 = ['beep','Beep bep','Bep beep','Bpep','Beep beep beeep','bep']
                fraseschewbacca = ['Grrrrowr','Hwaaurrgh','ghaawwu','huagg','Rrwaahhggg','Grrrruuughhh']
                if personaje == 'r2d2':
                    print(f"{personaje}:", random.choice(frasesr2d2))
                else:
                    print(f"{personaje}:", random.choice(fraseschewbacca))

            case 'yoda' | 'c-3po':
                if personaje == 'yoda':
                    respuesta = lectorPregunta(limpiadorFrases(entrada.lower().strip("¿?#$%&/()!¡")), True)
                else:
                    respuesta = lectorPregunta(limpiadorFrases(entrada.lower().strip("¿?#$%&/()!¡")), False)
                if respuesta == "No tengo respuesta para esa pregunta, lo siento. Vamos a agregar la pregunta al sistema.":
                    print(f"{personaje}:", respuesta)
                    agregarPregunta(entrada)
                    return inicioPrograma()
                print(f"{personaje}:", respuesta)

                    
             
def limpiadorFrases(input):
    palabraSimplificada = []
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
                    palabraSimplificada.append(palabra)
            palabra = ''
        else:
            palabra += letras

    if palabra:
        if palabra in articulos:
            pass
        else:
            palabraSimplificada.append(palabra)

    return palabraSimplificada
# Responder
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
            elif lineas == "":
                if quest:
                    questGroup.append(quest)
                    answGroup.append(answ)
                    quest = []
                    answ = []
   
    if agregoPregunta == True:
            questGroup.append(newQuest)
            answGroup.append(newAnsw)

    return buscarRespuesta(userInput, questGroup, answGroup)


# --- PROGRAMA PRINCIPAL ---
print("--------------------------------------------------------------")
print("          BIENVENIDO AL MEJOR ASISTENTE DE STAR WARS          ")
print("--------------------------------------------------------------")
print("Se inicio el chat, escriba su pregunta. Si desea finalizar el chat escriba salir o adios.")
print((1+2)//2)
inicioPrograma()




