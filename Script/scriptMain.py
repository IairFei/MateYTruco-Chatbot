"""En este archivo se ejecuta el programa principal, se importan las funciones necesarias y se ejecuta el programa."""

'''FALTA
1) revisar coherencia
2) consultar escritura archivos
3)hoja que guarde preguntas no respuestas

opcionales
1) arrays chewbaca y r2d2
2) nombre de usuario
'''

import random

yoda = False


def inicioPrograma():
    print("Podés chatear con distintos personajes como R2D2, Chewbacca, Yoda o C-3PO. Cuando desees cambiar de personaje, escribí: cambiar personaje: seguido del nombre.\n")
    personaje = input("Coloque el nombre del personaje con el que desea hablar: ")
    eleccionPersonaje(personaje)
def agregarPregunta():
    """Agrega una pregunta al archivo de preguntas.txt."""
    question = input("Escriba la pregunta que desea agregar:")

    if readQuest(question.lower().strip("¿?#$%&/()!¡"), False) != "No tengo respuesta para esa pregunta, lo siento. Si desea hacerme otra pregunta, porfavor escribala. En caso de querer agregar la pregunta al sistema, escriba: agregar pregunta.":
        print("La pregunta ya existe en el sistema.")
        nuevaPregunta = input("Desea agregar una nueva pregunta? (si/no): ")
        if nuevaPregunta.lower() == "si":
            return agregarPregunta()
        else:
            print("No se agrego la pregunta.")
            return inicioPrograma()
    with open("ArchivosDeLectura/preguntas.txt", "a", encoding="utf-8") as file:
        file.write(f"Q: {question}\n")
        answer = input("Escriba la respuesta que desea agregar:")
        file.write(f"A: {answer}\n")
        yodaAnswer = input("Desea agregar una respuesta de Yoda? (si/no):")
        if yodaAnswer.lower() == "si":
            yodaAnswer = input("Escriba la respuesta que desea agregar:")
            file.write(f"YA: {yodaAnswer}\n")
        file.write("\n")
        print("\nPregunta y respuesta agregadas correctamente.")
        return inicioPrograma()

def buscarRespuesta(userInput, questGroup, answGroup):
    """Busca la pregunta en el grupo de preguntas y devuelve la respuesta correspondiente."""

    for x in range(len(questGroup)):
        for y in range(len(questGroup[x])):
            if(questGroup[x][y] == userInput):
                return answGroup[x][0]

    return "No tengo respuesta para esa pregunta, lo siento. Si desea hacerme otra pregunta, porfavor escribala. En caso de querer agregar la pregunta al sistema, escriba: agregar pregunta."
def eleccionPersonaje(personaje):    
    match personaje.lower():

        case 'r2d2':
            frasesR2d2 = ['beep','Beep bep','Bep beep','Bpep','Beep beep beeep']
            while True:
                entrada = input("Tú: ")
                if entrada.lower() == "salir" or entrada.lower() == "adios" :
                    print("Conversación finalizada, que la fuerza te acompañe.")
                    break
                if entrada.lower() == "cambiar de personaje" or entrada.lower() == "cambiar personaje" :
                    personaje = input('Que personaje desea elegir: ')
                    eleccionPersonaje(personaje)
                print("R2D2:", random.choice(frasesR2d2))
                
        case 'chewbacca':
            frasesChew = ['Grrrrowr','Hwaaurrgh','ghaawwu','huagg','Rrwaahhggg','Grrrruuughhh']
            while True:
                entrada = input("Tú: ")
                if entrada.lower() == "salir" or entrada.lower() == "adios" :
                    print("Conversación finalizada, que la fuerza te acompañe.")
                    break
                if entrada.lower() == "cambiar de personaje" or entrada.lower() == "cambiar personaje" :
                    personaje = input('Que personaje desea elegir: ')
                    eleccionPersonaje(personaje)
                print("Chewbacca:", random.choice(frasesChew) ) 
        
        
        case 'yoda':
            while True:
                entrada = input("Tú: ")
                if entrada.lower() == "salir" or entrada.lower() == "adios" :
                    print("Conversación finalizada, Que la fuerza te acompañe, siempre.")
                    break
                elif entrada.lower() == "cambiar de personaje" or entrada.lower() == "cambiar personaje" :
                    personaje = input('Que personaje desea elegir: ')
                    eleccionPersonaje(personaje,)
                elif entrada.lower() == "agregar pregunta":
                    agregarPregunta()
                else:
                    respuesta = readQuest(entrada.lower().strip("¿?#$%&/()!¡"), True)
                print("Yoda:", respuesta)

        case 'c-3po':
            print("Hola, soy C-3PO, relaciones cibernéticas-humanas. Domino más de seis millones de formas de comunicación, hazme tu pregunta")
            while True:
                entrada = input("Tú: ")

                if entrada.lower() == "salir" or entrada.lower() == "adios" :
                    print("Conversación finalizada, que la fuerza te acompañe.")
                    break
                elif entrada.lower() == "cambiar de personaje" or entrada.lower() == "cambiar personaje" :
                    personaje = input('Que personaje desea elegir: ')
                    eleccionPersonaje(personaje,)
                elif entrada.lower() == "agregar pregunta":
                    agregarPregunta()
                else:
                    respuesta = readQuest(entrada.lower().strip("¿?#$%&/()!¡"), False)   
                print("C-3PO:", respuesta)
        
        case _:
            while True:
                entrada = input('No entendi, ingrese el personaje nuevamente: ')

                if entrada.lower() == "salir" or entrada.lower() == "adios" :
                    print("Conversación finalizada, que la fuerza te acompañe.")
                    break
                eleccionPersonaje(entrada)
                    

# Responder
def readQuest(userInput, yoda):
    
    questGroup = []
    answGroup = []
    quest = []
    answ = []
    
    with open("ArchivosDeLectura/preguntas.txt", "r", encoding="utf-8") as file:
    
        for lineas in file:
            lineas = lineas.strip()
            if lineas.startswith("Q:"):
                quest.append(lineas[3:].lower().strip("¿?#$%&/()¡!"))
            elif lineas.startswith("A:") and yoda == False:
                answ.append(lineas[3:])
            elif lineas.startswith("YA:") and yoda == True:
                answ.append(lineas[3:])               
            elif lineas == "":
                if quest:  
                    questGroup.append(quest)
                    answGroup.append(answ)
                    quest = []
                    answ = []
        return buscarRespuesta(userInput, questGroup, answGroup)



# --- PROGRAMA PRINCIPAL ---
print("--------------------------------------------------------------")
print("          BIENVENIDO AL MEJOR ASISTENTE DE STAR WARS          ")
print("--------------------------------------------------------------")
print("Se inicio el chat, escriba su pregunta. Si desea finalizar el chat escriba salir o adios.")
print("Porfavor no utilice tildes, Gracias.")
inicioPrograma()




