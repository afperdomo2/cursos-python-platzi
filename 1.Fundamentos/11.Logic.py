# Operadores lógicos

# 1. and
print("1. Operador: AND")
print("True and True:", True and True)  # True
print("True and False:", True and False)  # False
print("False and True:", False and True)  # False
print("False and False:", False and False)  # False

print(10 > 5 and 2 < 20)  # True
print(10 == 10 and 10 < 1)  # False

stock = input("➡️  Ingrese la cantidad de Stock:")
stock = int(stock)
print("Stock:", stock)

if stock >= 100 and stock <= 1000:
    print(f"✅ Stock ({stock}) Correcto")
else:
    print(f"😓 El Stock ({stock}) se está agotando")


# 1. or
print("\n2. Operador: OR")
print("True or True:", True or True)  # True
print("True or False:", True or False)  # True
print("False or True:", False or True)  # True
print("False or False:", False or False)  # False


role = input("➡️  Ingrese su rol:")
if role == "admin" or role == "seller":
    print(f"✅ Rol: {role}. Acceso correcto")
else:
    print(f"⛔ El rol {role}, no tiene permiso")
