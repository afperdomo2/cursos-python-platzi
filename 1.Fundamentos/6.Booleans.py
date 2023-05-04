# Booleans

is_single = True
is_single = False
print("is_single =>", is_single)

# El not invierte el valor
print("No es True:", not True)
print("No es False:", not False)

# Invertir el valor de un boolean
is_single = not is_single
print("Invertido:", is_single)

age = 30

# La función bool convierte un valor x en su equivalente booleano
# según el procedimiento de prueba de veracidad
print(bool(is_single))  # True
print(bool(age))  # True
print(bool(-1))  # True
print(bool(0))  # False
print(bool(None))  # False
print(bool("Casa"))  # True
print(bool(0.0))  # True
