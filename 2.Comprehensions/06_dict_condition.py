import random

countries = ["COL", "VEN", "PER"]
population = {country: random.randint(1, 100) for country in countries}
print(population)

result = {
    country: population for country, population in population.items() if population > 20
}
print(result)

text = "Hola mundo"
unique = {letter: letter.upper() for letter in text if letter in "aeiou"}
print(unique)
