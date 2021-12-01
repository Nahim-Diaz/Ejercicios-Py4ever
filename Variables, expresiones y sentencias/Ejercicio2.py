# Ejercicio: Escribe un programa para pedirle al usuario el número de horas y la tarifa por hora para calcular el salario bruto.
# Introduzca Horas: 35
# Introduzca Tarifa: 2.75
# Salario: 96.25

def main():
    horas = int(input("Introduzca el numero de Horas: "))
    tarifa = float(input("Introduzca la tarifa: "))
    print(f"Tu salario es: {round(horas*tarifa, 2)} dolares")

if __name__ == "__main__":
    main()