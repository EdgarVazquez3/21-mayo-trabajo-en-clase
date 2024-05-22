while True:
    email = input("Introduce tu email: ")
    if "edgar.mx" in email and "." in email:
        print("Email valido")
        break
    else:
        print("Email no valido ")