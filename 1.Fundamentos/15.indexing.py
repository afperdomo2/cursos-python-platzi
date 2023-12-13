text = "Ella sabe Python"
print(text[0])  # E
print(text[1])  # l
print(text[-1])  # n

# slicing
print(text[0:4])  # Ella
print(text[:4])  # Ella

print(text[10:16])  # Python
print(text[10:])  # Python

print(text[:])  # Ella sabe Python

# El tercer parámetro aplica un salto
print(text[10:16:2])  # Pto

# Aplicar salto a todo el texto
print(text[::2])  # ElsbePto
