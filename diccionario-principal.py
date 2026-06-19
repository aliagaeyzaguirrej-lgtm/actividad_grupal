#creamos el diccionario donde estaran los alumnos ya registrados y con sus materias con sus notas 
print("---ALUMNOS REGISTRADOS---")
sistema = {
    "Javier":{"matematicas":85, "Datos y algoritmos":40, "Habilidades TIC":84, "Hardware": 60, "Especificaciones y Requerimientos": 70},
    "Nataelio": {"matematicas":61, "Datos y algoritmos":70, "Habilidades TIC":26, "Hardware": 45, "Especificaciones y Requerimientos": 15},
    "Maria": {"matematicas":55, "Datos y algoritmos":90, "Habilidades TIC": 70, "Hardware": 90, "Especificaciones y Requerimientos": 88},
    "Adrian": {"matematicas": 76, "Datos y algoritmos": 60, "Habilidades TIC": 67,"Hardware": 20, "Especificaciones y Requerimientos": 48},
    "Alex":  {"matematicas": 83, "Datos y algoritmos": 40, "Habilidades TIC": 20, "Hardware": 46, "Especificaciones y Requerimientos": 79},
    "Luis": {"matematicas": 96, "Datos y algoritmos": 80, "Habilidades TIC": 92, "Hardware": 68, "Especificaciones y Requerimientos": 39}
}
#hacemos un for donde muestre los nombres de los aluumnos y sus materias con sus notas
#utilizamos dos variables y la función .items() para que python asigne una variable a los alumnos (los nombres de cada alumno) y notas (los mini diccionarios con las materias y notas)
for nombre, notas in sistema.items():
    print (f"el alumno {nombre} tiene las siguientes materias y notas: {notas}")
    
