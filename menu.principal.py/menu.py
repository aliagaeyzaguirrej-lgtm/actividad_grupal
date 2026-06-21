# Diccionario con alumnos registrados
alumnos_registrados= {
    "Juan": 0,
    "Maria": 0,
    "Pedro": 0,
    "Camila": 0
}
alumnos_nuevos = {}# Diccionario vacío para nuevos alumnos
while True: #while true para repetir el menu hasta el usuario desida salir
    print("\n MENÚ PRINCIPAL ") #con un print ingreso las opciones para el menu
    print("1.Ver alumnos registrados ")
    print("2.Añadir alumno ")
    print("3.Actualizar nota ")
    print("4.Calcular el promedio de las notas de un estudiante ")
    print("5.Salir ")
    opcion = input("Seleccione una opción: ") # con un imput creo una variable donde guarde las opciones
    if opcion == "1":
        print("Ver los datos de los alumnos... ")
    elif opcion == "2":
        print("Ingresa los datos para anadir alumnos ")
        # Aquí va el código para añadir o actualizar la tarea
    elif opcion == "3":
        print("r\n Actualizar nota")
        nombre = input("Ingrese el nombre del estudiante: ")
        if nombre not in alumnos_registrados:
            print("Estudiante no registrado...")
        else:
              asignatura = input ("igrese la asignatura: ")
              nota = float(input("Ingrese la nueva nota: "))
              if nota > 0:
                alumnos_registrados [nombre] [asignatura] = nota
                print( f" se registro la nueva {nota} en la {asignatura} ")
    elif opcion == "4":
        print("Ingrese los nuevos datos de los estudiantes")
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente nuevamente.") 