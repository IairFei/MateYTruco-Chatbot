
articulos = ["el","la","los","las","un","una","unos","unas","al","del"]
vocalesTildes = ["á", "é", "í", "ó", "ú"];

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
    #Busca la pregunta en el grupo de preguntas y devuelve la respuesta mas cercana.
    coincidenciaMax = 0
    position = 0

    for x in range(len(questGroup)):
        coincidenciaNow = 0
        for y in range(len(questGroup[x])):
            listQuest = simplificador(questGroup[x][y])
            for palabra in userInput:
                if palabra in listQuest:
                    coincidenciaNow += 1

        if coincidenciaNow > coincidenciaMax: #compara para saber cual es la maxima coincidencia
            coincidenciaMax = coincidenciaNow
            position = x

    if coincidenciaMax >= 1:
        return(print(answGroup[position][0]))
    else: 
        return(print("no entendí"))  # en caso de no entender la pregunta ejecuta la funcion de "agregar pregunta()"

def simplificador(input): # se encarga de volver cada palabra del string una posicion del array y quitarle todos los articulos que contenga
    palabraSimplificada = []
    palabra = ''
    for letras in input:
        if letras == " ":
            for art in articulos:
                if palabra != art:
                    palabraSimplificada.append(palabra)
                    palabra=''
        else:
            palabra += letras

    for art in articulos:
                if palabra == art or palabra == '':
                   break
                else: 
                    palabraSimplificada.append(palabra)
                    break

    return(palabraSimplificada)


while True:

    userInput = input("Escriba tu respuesta: ")
    if userInput == "salir":
        break
    else:
        readQuest(simplificador(userInput.lower()))