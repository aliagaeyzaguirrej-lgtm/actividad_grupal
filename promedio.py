sistema = {
    "Javier": {"matematicas":85, "Datos y algoritmos":40, "Habilidades TIC":80},
    "Nataelio": {"matematicas":60, "Datos y algoritmos":70, "Habilidades TIC":20},
    "Maria" : {"matematicas":50, "Datos y algoritmos":90, "Habilidades TIC": 70},
    "Adrian":{"matematicas": 70, "Datos y algoritmos": 60, "Habilidades TIC": 60}
}
sistema2 = {"Sofia": {"matematicas": 90, "Datos y algoritmos": 80, "Habilidades TIC": 85},
}


print(" (1) si quieres saber el promedio de los alumnos nuevos")
print(" (2) si quieres saber el promedio de un alumno ya registrado")
print(" (3) para salir del programa.")

while True:
    choice = input("Elige una opción: ")

    if choice == "3":
        print("Cerrando el programa. ")
        break



    elif choice == "1":
        while True:
            m = input("introduce el nombre del alumno nuevo  o 0 para salir").title()

            #busca si el nombre ingresado esta en el diccionario
            if m == "0":
                print("Cerrando el programa. ")
                break
            elif m in sistema2:
                print("Alumno encontrado.")
                #recorre con un for 
                for nota in sistema2[m].items(): #recorre los items del alumno Nuevo encontrado
                    promedio = sum(sistema2[m].values()) / len(sistema2[m]) #una variable
                    #que suma los valores del alumno y los divide por la cantidad de materias usando len
                #impimir los resultados llamando el alumno y el promedio
                print(f"promedio de {m} es: {promedio:.2f}")
                # print para mostrar resultados y se utiliza para mostrar hasta cuantos decimales mostrar
                break #break para cerrar el ciclo y volver al menu principal
            #repite la pregunta hasta que encuentre un alumno valido
            else:
                print("Alumno nuevo no encontrado. Inténtalo de nuevo")
        print(" (1) si quieres saber el promedio de los alumnos nuevos")
        print(" (2) si quieres saber el promedio de un alumno ya registrado")
        print(" (3) para salir del programa.")

    #Validador de alumnos pedido en consola
    elif choice == "2":
        while True:
            p = input("introduce el nombre del alumno o 0 para salir").title()

            if p == "0":
                print("Cerrando el programa.")
                break

        #busca si el nombre ingresado esta en el diccionario
            elif p in sistema:
                print("Alumno encontrado.")
                #recorre con un for 
                for nota in sistema[p].items(): #recorre los items del alumno encontrado
                    promedio = sum(sistema[p].values()) / len(sistema[p]) #una variable
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
