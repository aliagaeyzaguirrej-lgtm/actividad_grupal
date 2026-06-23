sistema = {
    "Javier": {"matematicas":85, "Datos y algoritmos":40, "Habilidades TIC":80},
    "Nataelio": {"matematicas":60, "Datos y algoritmos":70, "Habilidades TIC":20},
    "Maria" : {"matematicas":50, "Datos y algoritmos":90, "Habilidades TIC": 70},
    "Adrian":{"matematicas": 70, "Datos y algoritmos": 60, "Habilidades TIC": 60}
}
alumnos_nuevos = {"Sofia": {"matematicas": 90, "Datos y algoritmos": 80, "Habilidades TIC": 20},
}

#menu para elegir entre alumnos nuevos o ya registrados
print(" (1) si quieres saber el promedio de los alumnos nuevos")
print(" (2) si quieres saber el promedio de un alumno ya registrado")
print(" (3) para salir del programa.")

while True:
    choice = input("Elige una opción: ")

    if choice == "3":
        print("Cerrando el programa. ")
        break



    elif choice == "1":
        nombre = input("introduce el nombre del alumno nuevo ").title()
                #busca si el nombre ingresado esta en el diccionario

        if nombre in alumnos_nuevos: #busca si el nombre ingresado esta en el diccionario
            print("Alumno encontrado.")
            if len(alumnos_nuevos[nombre]) > 0: #verifica si el alumno tiene notas ingresadas 
                                   
                    notas = alumnos_nuevos[nombre].values()#toma las notas del alumno encontrado
                    promedio = sum(notas) / len(notas) #divide las notas totales por la cantidad de materias

            print(f"El promedio de {nombre} es: {promedio:.2f}")
        else:
            print(f"El alumno {nombre} no está registrado o no tiene notas ingresadas.")
                # print para mostrar resultados y se utiliza para mostrar hasta cuantos decimales mostrar
            break #break para cerrar el ciclo y volver al menu principal
            #repite la pregunta hasta que encuentre un alumno valido

    #Validador de alumnos pedido en consola
    elif choice == "2":
        while True:#while para repetir la pregunta hasta que encuentre un alumno valido
            p = input("introduce el nombre del alumno").title()
            #busca si el nombre ingresado esta en el diccionario
            if p in sistema:
                print("Alumno encontrado.")
                promedio =sum(sistema[p].values()) /  len(sistema[p]) #una variable
                #que suma los valores del alumno y los divide por la cantidad de materias usando len
            #impimir los resultados llamando el alumno y el promedio
                print(f"promedio de {p} es: {promedio:.2f}")# print para mostrar resultados y se utiliza para mostrar hasta cuantos decimales mostrar
                break #para salir del ciclo y volver al menu principal
            #repite la pregunta hasta que encuentre un alumno valido
            else:
                print("Alumno no encontrado. Inténtalo de nuevo")
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        print("=========================================")
