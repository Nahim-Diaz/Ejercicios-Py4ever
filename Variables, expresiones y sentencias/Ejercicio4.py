# Ejercicio: Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.

def main():
    celsius = int(input("¿A qué temperatura estas?: "))
    fareheint = celsius*(9/5)+32
    print(f"Tu temperatura actual es {celsius}°C o {fareheint}°F")


if __name__ == "__main__":
    main()