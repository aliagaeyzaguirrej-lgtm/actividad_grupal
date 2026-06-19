sistema = {
    "Javier": {"matematicas":85, "Datos y algoritmos":40, "Habilidades TIC":80},
    "Nataelio": {"matematicas":60, "Datos y algoritmos":70, "Habilidades TIC":20},
    "Maria" : {"matematicas":50, "Datos y algoritmos":90, "Habilidades TIC": 70},
    "Adrian":{"matematicas": 70, "Datos y algoritmos": 60, "Habilidades TIC": 60}
}

while True:
    p = input("introduce el nombre del alumno ").capitalize()

    if p in sistema:
        print("¡Acceso concedido!")
        for materia, nota in sistema[p].items():
            promedio = sum(sistema[p].values()) / len(sistema[p])

    else:
        print("Incorrecto. Inténtalo de nuevo.")
        
    print(f"promedio de {p} es: {promedio:.2f}")