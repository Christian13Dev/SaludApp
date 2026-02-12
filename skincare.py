from datetime import datetime

# 1. FUNCIÓN PARA CARGAR (Leer del archivo al empezar)
def cargar_cremas():
    try:
        with open("cremas.txt", "r") as archivo:
            # Leemos las líneas y quitamos espacios/saltos de línea
            return [linea.strip() for linea in archivo.readlines() if linea.strip()]
    except FileNotFoundError:
        # Si no hay archivo, devolvemos la lista por defecto
        return ["nivea", "aloe_vera", "avena"]

# 2. INICIALIZAMOS LA LISTA (Usando la función de carga)
cremas = cargar_cremas()

# 3. FUNCIÓN PARA VER
def ver_cremas():
    print("Aquí tienes una lista de cremas para cuidar tu piel.")
    for crema in cremas: # Usamos la lista que ya está en memoria
        print(f"Producto disponible: {crema.upper()}")

# 4. FUNCIÓN PARA GUARDAR (Escribir al salir)
def guardar_cremas():
    with open("cremas.txt", "w") as archivo:
        for crema in cremas:
            archivo.write(f"{crema}\n")

# --- Tus otras funciones de resumen y registro (están perfectas) ---
def ver_resumen():
    try:
        with open("registro_piel.txt", "r") as archivo_piel:
            lineas = archivo_piel.readlines()
            if lineas:
                print("Registro de aplicación de crema:")
                for linea in lineas:
                    print(linea.strip())
            else:
                print("No hay registros de aplicación de crema.")
    except FileNotFoundError:
        print("No se ha registrado ninguna aplicación de crema aún.")

def registrar_piel(horas_sin_crema):
    ahora = datetime.now()
    fecha_texto = ahora.strftime("%d/%m/%Y %H:%M:%S")
    with open("registro_piel.txt", "a") as archivo_piel:
        archivo_piel.write(f"[{fecha_texto}] Horas: {horas_sin_crema}\n")
    if horas_sin_crema > 3:
        print("¡Recuerda aplicar crema para mantener tu piel hidratada!")
    else:
        print("¡Bien hecho! Sigue cuidando tu piel.")