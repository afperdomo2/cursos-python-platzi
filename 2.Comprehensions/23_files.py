path = "./file.txt"

print("✅ 1. Leer archivo completo:")
file = open(path)
print(file.read())
file.close()  # Cerrar archivo


print("\n✅ 2. Leer linea por linea:")
file2 = open(path)
print(file2.readline())  # Lee la primera linea
print(file2.readline())  # Lee la segunda linea
print(file2.readline())  # Lee la tercera linea
file2.close()  # Cerrar archivo


print("\n✅ 3. Leer todas las lineas con un for:")
file3 = open(path)
for line in file3:
    print(line)
file3.close()  # Cerrar archivo


print("\n✅ 4. Leer todas las lineas con un with:")
# El with se encarga de cerrar el archivo automaticamente
with open("./file.txt") as file4:
    for line in file4:
        print(line)
