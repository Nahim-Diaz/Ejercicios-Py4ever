# Ejercicio: Reescribe el programa del cálculo del salario para darle al empleado
# 1.5 veces la tarifa horaria para todas las horas trabajadas que excedan de 40.

def main():
    horas = int(input("Introduzca el numero de Horas: "))
    tarifa = float(input("Introduzca la tarifa: "))
    salario = horas * tarifa
    if horas > 40:
        extra = tarifa *1.5
        salario = extra + (tarifa * horas)
    print(f"Tu salario es: {round(salario, 2)} dolares")



if __name__ == "__main__":
    main()