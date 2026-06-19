sistema = {
    "Javier": {"matematicas":85, "Datos y algoritmos":40, "Habilidades TIC":80},
    "Nataelio": {"matematicas":60, "Datos y algoritmos":70, "Habilidades TIC":20},
    "Maria" : {"matematicas":50, "Datos y algoritmos":90, "Habilidades TIC": 70},
    "Adrian":{"matematicas": 70, "Datos y algoritmos": 60, "Habilidades TIC": 60}
}

#Validador de alumnos pedido en consola
while True:
    p = input("introduce el nombre del alumno ").capitalize()

    #busca si el nombre ingresado esta en el diccionario
    if p in sistema:
        print("Alumno encontrado.")
        #recorre con un for 
        for nota in sistema[p].items(): #recorre los items del alumno encontrado
            promedio = sum(sistema[p].values()) / len(sistema[p]) #una variable
            #que suma los valores del alumno y los divide por la cantidad de materias usando len
        #impimir los resultados llamando el alumno y el promedio
        print(f"promedio de {p} es: {promedio:.2f}")
    #repite la pregunta hasta que encuentre un alumno valido
    else:
        print("Alumno no encontrado. Inténtalo de nuevo")

