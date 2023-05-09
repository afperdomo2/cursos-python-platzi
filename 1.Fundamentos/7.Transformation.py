# Transformación de tipos

name = "Felipe"
print("type:", type(name))

name = 12
print("type:", type(name))

name = True
print("type:", type(name))


print("Andrés" + "Perdomo")
print(10 + 30)

age = 30
print("Mi edad es " + str(age))
print(f"Mi edad es {age}")  # Formatea a string la variable

# Formatear directamente desde el input
age = int(input("➡️  Ingresa tu edad:"))
print("tipe:", type(age))


name = 'Juana'
print(name)
age = '10'
print(age)
total = int(age) + 10


template = f"Hola mi nombre es {name}, tengo {age} años y en 10 años tendré {str(total)} años"
print(template)
