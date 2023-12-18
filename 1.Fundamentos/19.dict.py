animals = {}
print(type(animals))

animals = {
    "gato": "🐱",
    "perro": "🐶",
    "ratón": "🐭",
}
print(animals)  # {'gato': '🐱', 'perro': '🐶', 'ratón': '🐭'}
print(len(animals))  # 3

print(animals["gato"])  # 🐱
print(animals.get("gato"))  # 🐱

print("gato" in animals)  # True
print("loro" in animals)  # False
