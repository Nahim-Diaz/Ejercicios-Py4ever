# Ejercicio: Reescribe el programa de cálculo del salario, con tarifa para las horas extras, y crea una 
# función llamada calculo_salario que reciba dos parámetros (horas y tarifa).

# Introduzca Horas: 45
# Introduzca Tarifa: 10
# Salario: 465.0

def calculo_salario(horas, tarifa):
    salario = horas * tarifa
    if horas > 40:
        extra = tarifa *1.5
        salario = extra + (tarifa * horas)
    print(f"Tu salario es: {round(salario, 2)} dolares")


def main():
    horas = int(input("Introduzca el numero de Horas: "))
    tarifa = float(input("Introduzca la tarifa: "))
    calculo_salario(horas, tarifa)


if __name__ == "__main__":
    main()
