
articulos = ["el", "la", "los", "las", "un", "una", "unos", "unas", "al", "del", "es", "de","que","en",'quien','cuando']
vocalesTildes = ["á", "é", "í", "ó", "ú"]
vocalesSinTilde = ['a','e','i','o','u']

def readQuest(userInputResumida):
    questGroup = []
    answGroup = []
    quest = []
    answ = []


    with open("ArchivosDeLectura/preguntas.txt", "r", encoding="utf-8") as file:
        for lineas in file:
            lineas = lineas.strip()
            if lineas.startswith("Q:"):
                quest.append(lineas[3:].lower().strip("¿?#$%&/()¡!"))
            elif lineas.startswith("A:"):
                answ.append(lineas[3:])
            elif lineas.startswith("YA:"):
                answ.append(lineas[3:])
            elif lineas == "":
                if quest:
                    questGroup.append(quest)
                    answGroup.append(answ)
                    quest = []
                    answ = []
   
    return buscarRespuesta(userInputResumida, questGroup, answGroup)

def buscarRespuesta(userInput, questGroup, answGroup):
    coincidenciaMax = 0
    mejorIndice = -1

    for i in range(len(questGroup)):
        coincidenciasActuales = 0
        for pregunta in questGroup[i]:
            palabrasPregunta = simplificador(pregunta)  # Simplificar la pregunta
            for palabra in userInput:
                if palabra in palabrasPregunta:
                    coincidenciasActuales += 1
                    
        if coincidenciasActuales > coincidenciaMax:  # Solo actualiza si se encuentran más coincidencias
            coincidenciaMax = coincidenciasActuales
            mejorIndice = i

    if mejorIndice != -1 and coincidenciaMax > 2:
        return answGroup[mejorIndice][0]
    else:
        return "no entendí"  

#La funcion de simplificador la utilizamos para pasar de un string a un array, convirtiendo todas las palabras de la oracion en posiciones dentro del mismo

def simplificador(input):
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
    print(palabraSimplificada)
    return 

while True:
    userInput = input("Escriba tu respuesta: ")
    if userInput == "salir":
        break
    else:
        
        print(simplificador(userInput.lower()))
