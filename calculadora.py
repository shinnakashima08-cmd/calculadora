print("Bienvenido a mi calculadora")

print("¿qué operación quierés realizar?")
print("1. suma")   
print("2. resta")
print("3. multiplicación")
print("4. división")

opcion = input("elegi una opción (1/2/3/4): ")


numero1 = float(input("Ingresá el primer número: "))
numero2 = float(input("Ingresá el segundo número: "))

print("Número 1:", numero1)
print("Número 2:", numero2)

suma = numero1 + numero2


resta = numero1 - numero2


multiplicacion = numero1 * numero2





if opcion == "1":
    print("La suma es:", round(suma, 2))
elif opcion == "2":
    print("La resta es:", round(resta, 2))
elif opcion == "3":
    print("la multiplicación es:", round(multiplicacion, 2))
elif opcion == "4":
    if numero2 == 0:
        print("Error: no se puede dividir por cero")
    else:
        division = numero1 / numero2
        print("La división es:", round(division, 2))
        
else:
    print("operacón invalisa") 