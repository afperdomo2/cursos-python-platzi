fruits = ["Apple", "Orange", "Banana"]
print(fruits)

fruits[-1] = "Banano"
print(fruits)

# Agregar un elemento al final de la lista
fruits.append("Mango")
print(fruits)

# Insertar un elemento en una posición específica
fruits.insert(0, "Strawberry")
print(fruits)

fruits.insert(2, "Pineapple")
print(fruits)

vegetales = ["Tomate", "Lechuga"]

print("\nMarket:")
market = fruits + vegetales
print(market, "\n")

# Consultar la posición de un elemento en la lista
index = market.index("Pineapple")
market[index] = "Piña"
print(market, "\n")

print("Borrar elementos:")
del market[:2]  # Borrar un rango de elementos
market.remove("Mango")
market.pop()  # Elimina el último elemento de la lista
market.pop(1)  # Eliminar un elemento en una posición específica
print(market)

market.reverse()  # Invertir el orden de los elementos
print(market)

numbers = [100, 1, 8, 999, 7]
numbers.sort()
print(numbers)  # Ordenar los elementos de la lista

alphabet = ["a", "z", "j", "b"]
alphabet.sort()
print(alphabet)
