# Comprehensions on dict
import random

dict = {}
for i in range(1, 5):
    dict[i] = i * 2
print(dict)  # {1: 2, 2: 4, 3: 6, 4: 8}

dict_2 = {i: i * 2 for i in range(1, 5)}
print(dict_2)  # {1: 2, 2: 4, 3: 6, 4: 8}

# Sin comprehensions
countries = ["COL", "VEN", "PER"]
population = {}
for country in countries:
    population[country] = random.randint(1, 100)

print(population)

# Con comprehensions
population_2 = {country: random.randint(1, 100) for country in countries}
print(population_2)

names = ["Juan", "Pedro", "María"]
ages = [30, 40, 50]
# La función zip() en Python toma dos iterables (como listas,
# tuplas o cadenas) y los combina en un objeto zip que contiene
# pares de elementos correspondientes de ambos iterables. Cada
# par de elementos se representa como una tupla.
people = {name: age for name, age in zip(names, ages)}
print(people)  # {'Juan': 30, 'Pedro': 40, 'María': 50}

people_list = list(zip(names, ages))
print(people_list)  # [('Juan', 30), ('Pedro', 40), ('María', 50)]

people_2 = {name: age * 2 for (name, age) in zip(names, ages)}
print(people_2)  # {'Juan': 30, 'Pedro': 40, 'María': 50}
