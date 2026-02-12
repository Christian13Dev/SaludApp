import skincare # Trae todo lo de skincare.py
import fitness # Trae todo lo de fitness.py
from datetime import datetime # Trae la función para saber la fecha y hora actual

# Crear un menú interactivo para mostrar ejercicios y cremas para la piel
def mostrar_menu():
    print("Bienvenido a tu guía de salud y bienestar.")
    print("1. Ver ejercicios")
    print("2. Ver cremas para la piel")
    print("3. Resumen de cuantas veces me he aplicado crema")
    print("4. Horas sin aplicar crema")
    print("5. Añadir ejercicio a mi rutina")
    print("6. Salir")

def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1, 2, 3, 4, 5 o 6): ")


# Opción 1. Ver ejercicios
        if opcion == "1":
            fitness.ver_ejercicios()




# Opción 2. Ver cremas para la piel
        elif opcion == "2":
            skincare.ver_cremas()


# Opción 3. Resumen de cuantas veces me he aplicado crema
        elif opcion == "3":
            skincare.ver_resumen()

# Opción 4. Horas sin aplicar crema
        elif opcion == "4":
            horas_sin_crema = float(input("¿Cuántas horas llevas sin aplicarte la crema?"))
            skincare.registrar_piel(horas_sin_crema)




# Opción 5. Añadir ejercicio a mi rutina
        elif opcion == "5":
            fitness.añadir_ejercicio()
# Opción 6. Salir y guardar la rutina en un archivo de texto
        elif opcion == "6":
            print("¡Gracias por usar la guía de salud y bienestar! ¡Cuídate!")
            
            fitness.guardar_ejercicios() # Guardamos la rutina en el archivo de texto

            skincare.guardar_cremas() # Guardamos las cremas en el archivo de texto
                
            # Rompemos el bucle para salir
            break
        else:
            print("Opción no válida. Por favor, elige 1, 2, 3, 4, 5 o 6.")
if __name__ == "__main__":
    ejecutar_menu()