for element in range(2, 7):
    print(element)

# Recorriendo una lista
my_list = [1, 2, 90, 4, 88, 3]
print("my_list:", my_list)
for num in my_list:
    print(num)

# Recorriendo tuplas
animals = ("gato", "perro", "caballo", "vaca")
print("animals:", animals)
for animal in animals:
    print(animal)

# Recorriendo diccionarios
product = {"name": "book", "quantity": 3, "price": 4.99, "stock": 10}
print("product:", product)
for key in product:
    print(key, "=>", product[key])

# Desestructurando diccionarios en el for
print("product:", product)
for key, value in product.items():
    print(key, "=>", value)

# Recorriendo una lista de diccionarios
people = [
    {"name": "John", "age": 23},
    {"name": "Jane", "age": 23},
    {"name": "Joe", "age": 24},
    {"name": "June", "age": 25},
]
print("people:", people)
for person in people:
    print(person["name"], "=>", person["age"])
