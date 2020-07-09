import pyperclip as clipboard
from playsound import playsound
from time import sleep

def crearDatos():
    temas = {}
    principal = ""
    c = 0
    while principal != "-1":
        c+=1
        print("Tema " + str(c) + "\n")
        subtemas = {}
        opc = ingresaFormato()
        while opc != "-1":
            criterio,puntaje = opc.split("|")
            puntaje_total = int(puntaje)
            subtemas[criterio] = puntaje_total
            print("Temas ingresados : %d\n"%(len(subtemas)))
            opc = ingresaFormato()
        temas["Tema " + str(c)] = subtemas
        principal = input("\nIngresar nuevo tema? Enter: \nIngrese -1 para terminar el programa: ")
    return temas

def calificarRubrica(dic):
    print("-"*10 + "Ingreso de calificaciones" + "-"*10)
    total = 0
    salida = ""
    for key in dic:#{"Tema1":{"Criterio1":nota_total,"Criterio2":nota_total},"Tema2":{"Criterio1":nota}}
        salida = salida + "\t"*3 + key + "\n"
        for criterio in dic[key]:
            estu = input("Cuanto saco sobre %s en: %s?"%(dic[key][criterio],criterio))
            total += int(estu)
            salida += criterio + "\t" + estu + "/" + str(dic[key][criterio]) + "\n"
    encabezado = "Calificacion Final    " + str(total) + "/100" + "\n"*2
    salida = encabezado + salida + "\n"*2
    print("-"*40)
    #Logica de copia y pega
    clipboard.copy(salida)
    print("La rubrica esta en el portapapeles")
    #return salida

def ingresaFormato():
    entrada = input("Ingresar el tema a evaludar|puntaje_total\nIngrese -1 para terminar tema: ")
    while not validaFormato(entrada):
        #print("Ingrese el tema a evaluar|puntaje total!")
        entrada = input("Please,Ingresar el tema a evaludar|puntaje_total\nIngrese -1 para terminar tema: ")
    return entrada

def validaFormato(entrada):
    return  ("|" in entrada and entrada.count("|")== 1) or entrada== "-1"

#a = crearDatos()
rubrica = {
    "Tema1":{
        "Correcto uso del for":20,
        "Correcto manejo del while":30
    },
    "Tema2":{
        "Establece correctamente la condicion":25,
        "Calcula correctamente la persistencia" : 25
    }
}
print("Inicio proceso de calificacion de deberes")
opcion = input("Desea calificar un deber ? enter|-1")
while opcion != "-1":
    calificarRubrica(rubrica)

    playsound("inicio.mp3")
    sleep(10)
    playsound("fin.mp3")

    opcion = input("Desea calificar un nuevo deber? enter|-1")
print("Los deberes han sido calificados")
"""
clipboard.copy(corregido)
playsound("inicio.mp3")
sleep(10)
playsound("fin.mp3")
sleep(18)
"""