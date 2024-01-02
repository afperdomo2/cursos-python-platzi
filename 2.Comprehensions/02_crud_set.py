countries = {"Venezuela", "UK", "México"}

size = len(countries)
print("Size of countries:", size)  # 3

print("Venezuela" in countries)  # True
print("China" in countries)  # False

# add
countries.add("China")
print(countries)  # {'Venezuela', 'UK', 'México', 'China'}
countries.add("China")
print(countries)  # {'Venezuela', 'UK', 'México', 'China'}

# update
countries.update({"Colombia", "Perú", "Perú"})
print(countries)  # {'Venezuela', 'UK', 'México', 'China', 'Colombia', 'Perú'}

# remove
countries.remove("UK")
countries.remove("China")
print(countries)  # {'México', 'Colombia', 'Perú'}

countries.discard("Venezuela")  # Elimina un elemento si existe
countries.discard("Canada")  # No hace nada
print(countries)  # {'México', 'Colombia', 'Perú'}

# Borra todos los elementos
countries.clear()
print(countries)
print(len(countries))  # 0
