# Ejercicio: Reescribe el programa de calificaciones del capítulo anterior usando una función llamada 
# calcula_calificacion, que reciba una puntuación como parámetro y devuelva una calificación como cadena.

def calcula_calificacion(calificación):
    if calificación < 0.0 or calificación >1.0:
        print("La nota esta fuera de rango")
    elif calificación >= 0.9:
        print("Sobresaliente")
    elif calificación >= 0.8:
        print("Notable")
    elif calificación >= 0.7:
        print("Bien")
    elif calificación >= 0.6:
        print("Suficiente")
    elif calificación < 0.6:
        print("Insuficiente")


def main():
    nota = input("Escribe una nota: ")
    nota = float(nota)
    calcula_calificacion(nota)

if __name__ == "__main__":
    main()



