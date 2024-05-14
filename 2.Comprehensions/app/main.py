import utils

keys, values = utils.get_population()

print("countries:", keys)
print("values:", values)

country = input("Enter a country: ")
population = utils.population_by_country(country)
print(f"Population of {country}: {population}")
