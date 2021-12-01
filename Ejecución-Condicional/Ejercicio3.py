# Ejercicio: Escribe un programa que solicite una puntuación entre 0.0 y 1.0. Si la
# puntuación está fuera de ese rango, muestra un mensaje de error. Si la puntuación
# está entre 0.0 y 1.0, muestra la calificación usando la tabla siguiente:

nota = input("Escribe una nota: ")
nota = float(nota)
if nota < 0.0 or nota >1.0:
    print("La nota esta fuera de rango")
elif nota >= 0.9:
    print("Sobresaliente")
elif nota >= 0.8:
    print("Notable")
elif nota >= 0.7:
    print("Bien")
elif nota >= 0.6:
    print("Suficiente")
elif nota < 0.6:
    print("Insuficiente")

    