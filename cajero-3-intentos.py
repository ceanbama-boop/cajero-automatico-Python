saldo = 500.000
pin_correcto = 2528
intentos = 0
max_intentos = 3


while intentos < max_intentos:
    pin_usuario = int(input("Ingrese su PIN: "))
    if pin_usuario == pin_correcto:
        monto = float(input("Ingrese el monto"))
        if monto <= saldo:
            saldo -= monto
            print("Retiro exitoso, su nuevo saldo es:", saldo)
        else: 
            print("Lo sentimos, fondos insuficientes.")
        break
    else:
        intentos += 1
        print(f"PIN incorrecto. Intento {intentos} de {max_intentos}")

if intentos == max_intentos:
    print("Tarjet bloqueada. Contacte al banco.")