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

newAnsw =[]
newQuest= [] 
yoda = False
agregoPregunta = False


def inicioPrograma():
    print("Podés chatear con distintos personajes como R2D2, Chewbacca, Yoda o C-3PO. Cuando desees cambiar de personaje, escribí: cambiar personaje: seguido del nombre.\n")
    personaje = input("Coloque el nombre del personaje con el que desea hablar: ")
    eleccionPersonaje(personaje)

def agregarPregunta(userInput):
    """Agrega una pregunta al archivo de preguntas.txt."""
    with open("ArchivosDeLectura/preguntas.txt", "a", encoding="utf-8") as file:
        global agregoPregunta
        agregoPregunta = True
        file.write("\n")
        file.write(f"\nQ: {userInput}\n")
        answer = input("Escriba la respuesta que desea agregar para la pregunta '" + userInput + "':")
        file.write(f"A: {answer}\n")

        global newAnsw
        global newQuest
        
        newQuest.append(userInput)
        newAnsw.append(answer)
        
        file.write("\n")
        print("\nPregunta y respuesta agregadas correctamente.")

def buscarRespuesta(userInput, questGroup, answGroup,newQuest, newAnsw):
    """Busca la pregunta en el grupo de preguntas y devuelve la respuesta correspondiente."""

    for x in range(len(questGroup)):
        for y in range(len(questGroup[x])):
            if(questGroup[x][y] == userInput):
                return answGroup[x][0]

    return "No tengo respuesta para esa pregunta, lo siento. Vamos a agregar la pregunta al sistema."
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
                    eleccionPersonaje(personaje)
                else:
                    userInput, questGroup, answGroup = readQuest(entrada.lower().strip("¿?#$%&/()!¡"), True)
                    respuesta = buscarRespuesta(userInput, questGroup, answGroup, newQuest, newAnsw)
                    if respuesta == "No tengo respuesta para esa pregunta, lo siento. Vamos a agregar la pregunta al sistema.":
                        print("Yoda: ",respuesta)
                        agregarPregunta(userInput)
                        return inicioPrograma()    
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
                    eleccionPersonaje(personaje)
                else:
                    userInput, questGroup, answGroup = readQuest(entrada.lower().strip("¿?#$%&/()!¡"), False)
                    respuesta = buscarRespuesta(userInput, questGroup, answGroup, newQuest, newAnsw)
                    if respuesta == "No tengo respuesta para esa pregunta, lo siento. Vamos a agregar la pregunta al sistema.":
                        print("C-3PO: ",respuesta)
                        agregarPregunta(userInput)
                        return inicioPrograma()        
                print("C-3PO:", respuesta)
        case ('salir') | ('adios'):
            print("Conversación finalizada, que la fuerza te acompañe.")
            return
        case _:
            while True:
                entrada = input('No entendi, ingrese el personaje nuevamente: ')

                if entrada.lower() == "salir" or entrada.lower() == "adios" :
                    print("Conversación finalizada, que la fuerza te acompañe.")
                    break
                eleccionPersonaje(entrada)
    """inicioPrograma()  """              

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
        if agregoPregunta == True:
            questGroup.append(newQuest)
            answGroup.append(newAnsw)
        return (userInput, questGroup, answGroup)



# --- PROGRAMA PRINCIPAL ---
print("--------------------------------------------------------------")
print("          BIENVENIDO AL MEJOR ASISTENTE DE STAR WARS          ")
print("--------------------------------------------------------------")
print("Se inicio el chat, escriba su pregunta. Si desea finalizar el chat escriba salir o adios.")
print("Porfavor no utilice tildes, Gracias.")
inicioPrograma()




