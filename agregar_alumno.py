sistema = {
    "Javier":{"matematicas":8.5, "Datos y algoritmos":4, "Habilidades TIC":7, "Hardware": 6, "Especificaciones y Requerimientos": 7},
    "Nataelio": {"matematicas":6.1, "Datos y algoritmos":7, "Habilidades TIC":6, "Hardware": 5, "Especificaciones y Requerimientos": 1.5},
    "Maria": {"matematicas":5.5, "Datos y algoritmos":6.6, "Habilidades TIC": 7, "Hardware": 3, "Especificaciones y Requerimientos": 7},
    "Adrian": {"matematicas": 7, "Datos y algoritmos": 6, "Habilidades TIC": 6,"Hardware": 2, "Especificaciones y Requerimientos": 4},
    "Alex":  {"matematicas": 5, "Datos y algoritmos": 4, "Habilidades TIC": 2, "Hardware": 4, "Especificaciones y Requerimientos": 7},
    "Luis": {"matematicas": 6, "Datos y algoritmos": 5.5, "Habilidades TIC": 2, "Hardware": 6, "Especificaciones y Requerimientos": 3}
}
alumnos_nuevos = {}
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