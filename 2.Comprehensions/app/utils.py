def get_population():
    keys = ["COL", "BRA", "USA", "CAN"]
    values = [49, 209, 331, 37]
    return keys, values


def population_by_country(country):
    keys, values = get_population()
    countries = dict(zip(keys, values))
    return countries if country is None else countries.get(country)
