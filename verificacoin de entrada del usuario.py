while True:
    entrada = input("Introduce un numero entero: ")
    if entrada.isdigit():
        numero = int(entrada)
        print("El numero entero es",numero)
        break
    else:
        print("Error: entrada no valida")