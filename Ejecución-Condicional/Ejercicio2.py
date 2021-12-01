# Ejercicio: Reescribe el programa del salario usando try y except, de modo que el 
# programa sea capaz de gestionar entradas no numéricas con elegancia, mostrando un 
# mensaje y saliendo del programa. A continuación se muestran dos ejecuciones del programa

def main():
    horas = input("Introduzca el numero de Horas: ")
    tarifa = input("Introduzca la tarifa: ")
    try:
        horas = int(horas)
        tarifa = float(tarifa)
        salario = horas * tarifa
        if horas > 40:
            extra = tarifa *1.5
            salario = extra + (tarifa * horas)
        print(f"Tu salario es: {round(salario, 2)} dolares")
        
    except:
        print("Error, por favor digite un numero")
    

if __name__ == "__main__":
    main()