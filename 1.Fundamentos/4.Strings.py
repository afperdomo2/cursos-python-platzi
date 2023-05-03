# Strings

name = "Felipe"
last_name = "Perdomo"
full_name = name + " " + last_name

print("\nfull_name:", full_name)

print(f"""\nfull_name: {name} {last_name}""")

# Format
quote = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print("\nquote:", quote)

quote2 = f"Hola, mi nombre es {name} y mi apellido {last_name}"
print("\nquote2:", quote2)
