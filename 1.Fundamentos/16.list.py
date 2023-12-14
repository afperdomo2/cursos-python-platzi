numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)
print(type(numbers))

tasks = ["Comer", "Lavar los platos", "jugar", "Dormir"]
print(tasks)

print(numbers[0])
print(numbers[:3])  # Imprimir rangos
print(tasks[0])


tasks[0] = "Salir a pasear"
tasks[2] = "Jugar en el parque"
print(tasks)

if "Dormir" in tasks:
    print("Dormir esta en la lista")
