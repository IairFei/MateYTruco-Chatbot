import tkinter as tk
from tkinter import PhotoImage



"""def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Mi Aplicación Tkinter")
    root.geometry("300x200")

    # Crear un botón
    button = tk.Button(root, text="Haz clic aquí", command=lambda: print("¡Botón presionado!"))
    button.pack(pady=20)
    # Crear una etiqueta
    label = tk.Label(root, text="Hola, Tkinter!")
    label.pack(pady=10)
    # Crear un campo de entrada
    entry = tk.Entry(root)
    entry.pack(pady=10)
    # Crear un cuadro de texto
    text = tk.Text(root, height=5, width=30)
    text.pack(pady=10)
    # Crear un cuadro de lista
    listbox = tk.Listbox(root)
    listbox.pack(pady=10)
    # Agregar elementos a la lista
    listbox.insert(tk.END, "Elemento 1")
    listbox.insert(tk.END, "Elemento 2")
    listbox.insert(tk.END, "Elemento 3")
    # Crear un menú
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Nuevo")
    filemenu.add_command(label="Abrir")
    filemenu.add_command(label="Guardar")
    filemenu.add_separator()
    filemenu.add_command(label="Salir", command=root.quit)
    menubar.add_cascade(label="Archivo", menu=filemenu)
    root.config(menu=menubar)
    # Crear un marco
    frame = tk.Frame(root)
    frame.pack(pady=10)
    # Crear un botón dentro del marco
    frame_button = tk.Button(frame, text="Botón en marco", command=lambda: print("¡Botón en marco presionado!"))
    frame_button.pack(pady=10)
    # Crear un menú desplegable
    dropdown_var = tk.StringVar()
    dropdown_var.set("Opción 1")
    dropdown = tk.OptionMenu(root, dropdown_var, "Opción 1", "Opción 2", "Opción 3")
    dropdown.pack(pady=10)
    # Crear un cuadro de verificación
    check_var = tk.BooleanVar()
    checkbutton = tk.Checkbutton(root, text="Opción 1", variable=check_var)
    checkbutton.pack(pady=10)
    # Crear un cuadro de radio
    radio_var = tk.StringVar()
    radio_var.set("Opción 1")
    radiobutton1 = tk.Radiobutton(root, text="Opción 1", variable=radio_var, value="Opción 1")
    radiobutton2 = tk.Radiobutton(root, text="Opción 2", variable=radio_var, value="Opción 2")
    radiobutton1.pack(pady=10)
    radiobutton2.pack(pady=10)
    tk.mainloop()

main()"""
# Iniciar el bucle principal
"""tk.mainloop()"""
# root.mainloop()

"""def main():
    #Inicia el programa y solicita al usuario el personaje con el que desea interactuar.
    print("Bienvenido a la aplicación de chat con personajes de Star Wars.\n")
    print("Podés chatear con distintos personajes como R2D2, Chewbacca, Yoda o C-3PO. Cuando desees cambiar de personaje, escribí: cambiar personaje.\n")
    personaje = simpledialog.askstring("Personaje","Coloque el nombre del personaje con el que desea hablar:")
    #personaje = tk.simpledialog.askstring("Coloque el nombre del personaje con el que desea hablar:")
    tk.messagebox.showinfo("Personaje", f"Has elegido hablar con {personaje}.")
    tk.mainloop()
main()"""
"""  personaje = input("Coloque el nombre del personaje con el que desea hablar: ")"""
    
    
"""   eleccionPersonaje(personaje)"""


def seleccionar(personaje):
    # Esta función se llama cuando se selecciona un personaje
    print(f"Has seleccionado a {personaje}.")
    # Aquí puedes agregar la lógica para interactuar con el personaje seleccionado
    # Por ejemplo, abrir una nueva ventana o iniciar una conversación
    # ventana.destroy()  # Cierra la ventana actual
    # mostrar_segunda_ventana()  # Muestra la segunda ventana
    return personaje
    
def mostrar_segunda_ventana():
    segunda = tk.Tk()
    segunda.geometry("736x414")
    segunda.title("Asistente de Star Wars")

    resultado = tk.StringVar()

    canvas = tk.Canvas(segunda, width=736, height=414)
    canvas.pack()

    background_image = PhotoImage(file="Imagenes/StarWars.png")
    canvas.create_image(0, 0, image=background_image, anchor="nw")

    canvas.create_text(368, 100, text="Selecciona el personaje con el que deseas hablar",
                       fill="yellow", font=("Calibri", 20, "bold"), anchor="center")
    # Crear botones para cada personaje
    personajes = ["Yoda", "C-3PO", "R2D2", "Chewbacca"]
    for i, personaje in enumerate(personajes):
        tk.Button(segunda, text=personaje, bg="black", fg="white",
                  command=lambda p=personaje: seleccionar(p)).place(relx=0.5, rely=0.45 + i * 0.1, anchor="center", width=120, height=30)
    segunda.mainloop()


def inicio():
    ventana = tk.Tk()
    ventana.geometry("736x414")
    ventana.title("Asistente de Star Wars")

    resultado = tk.StringVar()

    canvas = tk.Canvas(ventana, width=736, height=414)
    canvas.pack()

    background_image = PhotoImage(file="Imagenes/StarWars.png")
    canvas.create_image(0, 0, image=background_image, anchor="nw")

    canvas.create_text(368, 100, text="BIENVENIDO AL ASISTENTE DE STAR WARS",
                       fill="yellow", font=("Calibri", 20, "bold"), anchor="center")

    def seleccionar(valor):
        resultado.set(valor)
        ventana.destroy()  # Cierra la primera ventana

    tk.Button(ventana, text="Iniciar", bg="black", fg="white",
              command=lambda: seleccionar("iniciar")).place(relx=0.5, rely=0.45, anchor="center", width=120, height=30)

    tk.Button(ventana, text="Salir del programa", bg="black", fg="white",
              command=lambda: seleccionar("salir")).place(relx=0.5, rely=0.55, anchor="center", width=120, height=30)

    tk.Button(ventana, text="Créditos", bg="black", fg="white",
              command=lambda: seleccionar("creditos")).place(relx=0.5, rely=0.85, anchor="center", width=70, height=30)

    ventana.mainloop()

    return resultado.get()

# Uso:


import random

#Librerias originales

articulos = ["el", "la", "los", "las", "un", "una", "unos", "unas", "al", "del", "es", "de","que","en","quien","por","para","con","a","y","o","si","no","como","mas","menos","muy","todo","toda","todos","todas"]

vocalesTildes = ["á","é","í","ó","ú"]
vocalesSinTilde = ['a','e','i','o','u']

#Globales
#Se declaran variables globales para almacenar las preguntas y respuestas nuevas que se agregan al sistema.

newAnsw =[]
newQuest= [] 
esYoda = False
agregoPregunta = False
primeraVez = True


def inicioPrograma():
    #Inicia el programa y solicita al usuario el personaje con el que desea interactuar.
    print("Podés chatear con distintos personajes como R2D2, Chewbacca, Yoda o C-3PO. Cuando desees cambiar de personaje, escribí: cambiar personaje: seguido del nombre.\n")
    personaje = input("Coloque el nombre del personaje con el que desea hablar: ")
    eleccionPersonaje(personaje)

def agregarPregunta(userInput):
    #Agrega una pregunta al archivo de preguntas.txt
    with open("ArchivosDeLectura/preguntas.txt", "a", encoding="utf-8") as file:
        agrPregunta = input("Deseea agregar la pregunta '"+ userInput +"' al sistema? (si/no):").lower().strip("¿?#$%&/()!¡-_[]{}.,;:<> ")
        #Se le pregunta al usuario si desea agregar la pregunta al sistema.
        #Si la respuesta es afirmativa, se le solicita la respuesta y se agrega al archivo preguntas.txt.
        #Si la respuesta es negativa, se le informa al usuario que no se agregará la pregunta."""
        
        while agrPregunta != "si" and agrPregunta != "no":
            agrPregunta = input("No entendí, ¿desea agregar la pregunta al sistema? (si/no):").lower().strip("¿?#$%&/()!¡ -_[]{}.,;:<>")
        
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


def eleccionPersonaje(personaje):
    #Permite al usuario elegir un personaje y mantener una conversación con él.
    while True:

        if personaje.lower() in ["salir", "adios"]:
            #Si el usuario ingresa 'salir' o 'adios', se finaliza la conversación.
            print("Conversación finalizada, que la fuerza te acompañe.")
            break

        if personaje.lower() not in ['yoda', 'chewbacca', 'r2d2', 'c-3po'] or personaje == '':
            #Si el personaje ingresado no es válido, se solicita nuevamente al usuario que ingrese un personaje
            personaje = input('No entendí, ingrese el personaje nuevamente: ')
            continue
        global primeraVez
        if primeraVez == True:
            print(f"\nElegiste hablar con {personaje}. Puedes hacerle preguntas o cambiar de personaje escribiendo 'cambiar personaje'.")
            print("Escribe 'salir' o 'adios' para finalizar la conversación.")
        entrada = input("Tú: ")

        if entrada.lower() in ["salir", "adios"]:
            #Si el usuario ingresa 'salir' o 'adios', se finaliza la conversación
            print("Conversación finalizada, que la fuerza te acompañe.")
            break

        if entrada.lower() in ["cambiar de personaje", "cambiar personaje"] :
            #Si el usuario desea cambiar de personaje, se solicita el nuevo personaje
            personaje = input('¿Qué personaje desea elegir? ')
            primeraVez = True
            continue
        #Se utiliza un bloque match para determinar el personaje elegido y responder en consecuencia.

        if entrada.lower() == '':
            #Si el usuario no ingresa nada, se le solicita que ingrese una pregunta
            primeraVez = False
            print("No entendí, por favor escriba una pregunta.")
            continue

        match personaje.lower():
            case 'r2d2' | 'chewbacca':
                #Si el personaje es R2D2 o Chewbacca, se generan frases aleatorias para cada uno.
                #Se utilizan listas de frases predefinidas para cada personaje y se elige una al azar
                primeraVez = False
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
                primeraVez = False
                if personaje == 'yoda':
                    respuesta = lectorPregunta(limpiadorFrases(entrada.lower().strip("¿?#$%&/()!¡-_[]}{.,;:<>")), True)
                else:
                    respuesta = lectorPregunta(limpiadorFrases(entrada.lower().strip("¿?#$%&/()!¡-_[]}{.,;:<>")), False)

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
respuesta = inicio()
if respuesta == "iniciar":
    mostrar_segunda_ventana()
elif respuesta == "creditos":
    print("Créditos: Este programa fue creado por [Tu Nombre].")
elif respuesta == "salir":
    print("Saliendo del programa...")
