print("Bienvenido a mi calculadora")

while True:
    print("¿qué operación querés realizar?")
    print("1. suma")
    print("2. resta")
    print("3. multiplicación")
    print("4. división")

    opcion = input("elegí una opción (1/2/3/4): ")

    numero1 = float(input("Ingresá el primer número: "))
    numero2 = float(input("Ingresá el segundo número: "))

    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2

    if opcion == "1":
        print("La suma es:", round(suma, 2))
    elif opcion == "2":
        print("La resta es:", round(resta, 2))
    elif opcion == "3":
        print("La multiplicación es:", round(multiplicacion, 2))
    elif opcion == "4":
        if numero2 == 0:
            print("Error: no se puede dividir por cero")
        else:
            division = numero1 / numero2
            print("La división es:", round(division, 2))
    else:
        print("Opción inválida")

    continuar = input("¿Querés hacer otra operación? (si/no): ")
    if continuar == "no":
        break