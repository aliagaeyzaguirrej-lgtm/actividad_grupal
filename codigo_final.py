#creamos el diccionario principal donde estaran los alumnos ya registrados
print("---ALUMNOS REGISTRADOS---")
sistema = {
    "Javier":{"matematicas":8.5, "Datos y algoritmos":4, "Habilidades TIC":7, "Hardware": 6, "Especificaciones y Requerimientos": 7},
    "Nataelio": {"matematicas":6.1, "Datos y algoritmos":7, "Habilidades TIC":6, "Hardware": 5, "Especificaciones y Requerimientos": 1.5},
    "Maria": {"matematicas":5.5, "Datos y algoritmos":6.6, "Habilidades TIC": 7, "Hardware": 3, "Especificaciones y Requerimientos": 7},
    "Adrian": {"matematicas": 7, "Datos y algoritmos": 6, "Habilidades TIC": 6,"Hardware": 2, "Especificaciones y Requerimientos": 4},
    "Alex":  {"matematicas": 5, "Datos y algoritmos": 4, "Habilidades TIC": 2, "Hardware": 4, "Especificaciones y Requerimientos": 7},
    "Luis": {"matematicas": 6, "Datos y algoritmos": 5.5, "Habilidades TIC": 2, "Hardware": 6, "Especificaciones y Requerimientos": 3}
}
#este diccionario vacio sirve para llenarlo con el estudiante nuevo y con sus materias y notas
alumnos_nuevos = {}
while True: #while true para repetir el menu hasta el usuario desida salir
    print("\n MENÚ PRINCIPAL ") #con un print ingreso las opciones para el menu
    print("1.VER ALUMNOS NUEVOS Y YA REGISTRADOS ")
    print("2.AÑADIR A ALUMNO NUEVO")
    print("3.AÑADIR NOTA A ALUMNO NUEVO ")
    print("4.CALCULAR EL PROMEDIO")
    print("5.SALIR DEL PROGRAMA")
    opcion = input("Seleccione una opción: ") # con un imput creo una variable donde guarde las opciones
    if opcion == "1":
        #en la opcion 1 hacemos un for donde las variables nombre y nota sean la llave y valor del diccionario llenado
        #de sistema 
        print("VER ALUMNOS NUEVOS Y YA REGISTRADOS ")
        for nombre, notas in sistema.items():#el .items() nos ayuda a asignar las variables como llave y valor del diccionario
            print(f"el alumno {nombre}")
            for materia, nota in notas.items():
                   #hacemos otro for que recorra los mini diccionarios y de las llaves y valores con las variables de materia y  nota 
                   print (f" {materia} ; {nota}")
            #convalidamos que el diccionario de estudiantes nuevos este vacio
        if len(alumnos_nuevos) == 0: # aqui validamos en el diccionario de alumnos_nuevos esta vacio
            print("NO HAY ESTUDIANTES NUEVOS")
        #una vez que en la opción de añadir nuevos estudiantes llene el diccionario vacio lo comprobamos con el else
        else:
            #recorremos en estudinates_nuevos con un for despues de que se haya llenado el diccionario vacio 
            for nombre, notas in alumnos_nuevos.items():
                print("\n Estudiante nuevo: ", nombre)
                    #aqui verificamos si el estudinate tiene una nota o no        
                if len(notas) == 0:#aqui validamos si el estudiante encontrado tiene una nota
                    print("No tiene notas registradas")
                        #y aqui mostramos las asignatutas y sus respectivas notas del alumno buscado en el nuevo estudiante 
                else:
                    for asignatura, nota in notas.items():#aqui asignamos como llave y valor con la función de .items() aignatura y nota
                        print(f"{asignatura} :  {nota}")

    elif opcion == "2":
        print("AÑADIR A ALUMNOS NUEVOS")
        print("Ingresa los datos para anadir alumnos ")
        # Aquí va el código para añadir al alumno
        nombre = input("Ingrese el nombre del estudiante: ").title()
        if nombre in alumnos_nuevos:#aqui validamos que si ya esta el nombre este en alumnos_nuevos
            print("el estudiante ya existe")
        elif nombre in sistema:#aqui validamos que si ya esta el nombre este en
            print("el estudiante ya existe")
        else:
            alumnos_nuevos[nombre] = {}#aqui agregamos el nombre al diccionario vacio 
            print("ESTUDIANTE AÑADIDO CORRECTAMENTE")
    elif opcion == "3":
        print("\n agregar nota a los alumnos nuevos")
        nombre = input("Ingrese el nombre del estudiante: ").title()
       
        if nombre not in  alumnos_nuevos:#verificamos si en nombre ya esta o no esta registrado
            print("ESTUDIANTE NO REGISTRADO...")
        else:
              asignatura = input ("igrese la asignatura: ")#aqui asignamos su materia 
              nota = float(input("Ingrese la nueva nota: "))#aqui asignamos su nota a la matria dada
              if nota > 0:#validamos que el numero sea mayor a cero
                alumnos_nuevos [nombre] [asignatura] = nota#aqui agregamos la materia y la nota al diccionario
                print( f" se registro la nota {nota} en la asignatura {asignatura} ")
              else:
                  print("NOTA INVALIDA INGRESE MAYOR A CERO")
    elif opcion == "4":
        print("CALCULAR EL PROMEDIO DE UN ESTUDIANTE")
        #usamos un while true para que repita este mini menu para calcular la nota
        while True:
                print(" (1) SI QUIERE SABER EL PROMEDIO DE UN ALUMNO NUEVO")
                print(" (2) SI QUIERE SABER EL PROMEDIO DE UN ALUMNO YA REGISTRADO")
                print(" (3) PARA SALIR AL MENU PRINCIPAL.")

                choice = input("SELECCIONE UNA OPCIÓN: ")

                if choice == "3":
                    print("DEVOLVIENDO AL MENU PRINCIPAL. ")#aqui si el usuario escoge la opcion 3 te devuelve al menu principal
                    break
                elif choice == "1":
        
                    nombre = input("introduce el nombre del alumno nuevo: ").title()

                #busca si el nombre ingresado esta en el diccionario
                    if nombre in alumnos_nuevos:#validamos si el nombre esta en alumnos_nuevos 
                        print("---ALUMNO ENCONTRADO---")
                        if len(alumnos_nuevos[nombre]) > 0:#verificamos que tenga nota el alumno
                            
                        
                            notas = alumnos_nuevos[nombre].values()#aqui llamamos a las notas o valores de alumno nuevo
                            promedio = sum(notas) / len(notas)#aqui sumamos las notas con la funcion sum y las dividimos entre la suma de cuantas notas hay
                            print(f"El promedio de {nombre} es: {promedio}")
                        
                    else:
                        print(f"El alumno {nombre} no está registrado o no tiene notas ingresadas.")
                

                        #repite la pregunta hasta que encuentre un alumno valido
                   
    #Validador de alumnos pedido en consola
                if choice == "2":
                    while True:#while para repetir la pregunta hasta que encuentre un alumno valido
                        p = input("introduce el nombre del alumno ya registrado: ").title()

                    #busca si el nombre ingresado esta en el diccionario
                        if p in sistema:#aqui verificamos si p esta en el diccionario principal
                            print("---ALUMNO ENCONTRADO---")
                    
                            promedio = sum(sistema[p].values()) / len(sistema[p]) # sumamos total de notas y divide por cantidad de notas
                            #que suma los valores del alumno y los divide por la cantidad de materias usando len
                            #impimir los resultados llamando el alumno y el promedio
                            print(f"promedio de {p} es: {promedio}")
                            break 
                    # print para mostrar resultados y se utiliza para mostrar hasta cuantos decimales mostrar
                    #repite la pregunta hasta que encuentre un alumno valido
                        else:
                            print("ALUMNO NO ENCONTRADO. INTENTELO DE NUEVO")
                else:
                    print("Opción no válida. Inténtalo de nuevo.")
                    print("=========================================")

    elif opcion == "5":
        print("SALIENDO DEL PROGRAMA...")
        break#aqui cerramos el programa 
    else:
        print("OPCIÓN NO VALIDA.") 