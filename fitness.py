# 1. FUNCIÓN PARA CARGAR (Leer al abrir el programa)
def cargar_ejercicios():
    try:
        with open("mi_rutina.txt", "r") as archivo:
            lineas = archivo.readlines()
            lista_nueva = []
            for linea in lineas[1:]:  # Saltamos el título
                texto = linea.replace("- ", "").strip()
                partes = texto.split(" (")
                nombre = partes[0]
                reps = int(partes[1].split(" ")[0])
                lista_nueva.append({"nombre": nombre, "repeticiones": reps})
            return lista_nueva
    except (FileNotFoundError, IndexError, ValueError):
        # Si el archivo no existe o falla, devolvemos la base
        return [
            {"nombre": "Sentadillas", "repeticiones": 15},
            {"nombre": "Flexiones", "repeticiones": 10},
            {"nombre": "Abdominales", "repeticiones": 20}
        ]

# 2. INICIALIZAMOS LA LISTA (Llamamos a la carga)
ejercicios = cargar_ejercicios()

# 3. FUNCIÓN PARA VER
def ver_ejercicios():
    print("\n--- Tu rutina actual ---")
    for ej in ejercicios:
        print(f"Ejercicio: {ej['nombre']} - Repeticiones: {ej['repeticiones']}")

# 4. FUNCIÓN PARA AÑADIR
def añadir_ejercicio():
    nombre = input("¿Qué ejercicio quieres añadir? ")
    reps = int(input("¿Cuántas repeticiones? "))
    nuevo = {"nombre": nombre, "repeticiones": reps}
    ejercicios.append(nuevo)
    print(f"¡{nombre} añadido!")

# 5. FUNCIÓN PARA GUARDAR (Escribir al salir)
def guardar_ejercicios():
    with open("mi_rutina.txt", "w") as archivo:
        archivo.write("Mi rutina de ejercicios:\n")
        for ej in ejercicios:
            archivo.write(f"- {ej['nombre']} ({ej['repeticiones']} repeticiones)\n")