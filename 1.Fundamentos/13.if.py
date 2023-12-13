if True:
    print("Se cumple la condición")
else:
    print("No se cumple la condición")

pet = input("\n🐶 Introduce tu mascota favorita: ")

if pet == "perro":
    print("Tienes un perro como mascota")
elif pet == "gato":
    print("Tienes un gato como mascota")
else:
    print("No tienes ni perro ni gato como mascota")


stock = int(input("\n🛒 Digita el stock de un producto: "))
if stock >= 100 and stock <= 1000:
    print(f"El stock es correcto ({stock})")
else:
    print(f"El stock NO es correcto ({stock})")


number = int(input("\n 🚀 Ingresa un número entero: "))
isEven = number % 2 == 0
if isEven:
    print(f"El número {number} es par")
else:
    print(f"El número {number} es impar")
