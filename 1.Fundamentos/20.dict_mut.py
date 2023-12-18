person = {
    "name": "Pepito",
    "last_name": "Perez",
    "langs": ["Python", "JavaScript"],
    "age": 30,
}
print(person, "\n")

person["name"] = "Pedro"
person["age"] -= 10
person["langs"].append("Go")
print(person, "\n")

# Borra un elementos de un diccionario
del person["last_name"]
person.pop("age")
print(person, "\n")

# Convierte un diccionario en una lista de tuplass
print(person.items(), "\n")

# Convierte un diccionario en una lista de claves
print(person.keys(), "\n")

# Convierte un diccionario en una lista de valores
print(person.values(), "\n")
