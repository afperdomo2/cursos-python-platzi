import utils


def run():
    keys, values = utils.get_population()

    print("countries:", keys)
    print("values:", values)

    country = input("Enter a country: ")
    population = utils.population_by_country(country)
    print(f"Population of {country}: {population}")


# Esta condición se utiliza para que el código solo se ejecute si se ejecuta el archivo main.py
if __name__ == "__main__":
    run()
