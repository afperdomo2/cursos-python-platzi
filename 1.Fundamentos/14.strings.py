text = "Ella sabe programar en Python"
print("JavaScript" in text)
print("Python" in text)

if "Python" in text:
    print("Sabe programar en Python")
else:
    print("No sabe programar en Python")

size = len("amor      ")
print("\nSize:", size)

print("\n✅ Convertir a mayúsculas:")
print(text)
print(text.upper())

print("\n✅ Convertir a minúsculas:")
print(text)
print(text.lower())

# nContar repeticiones (a)
print(text.count("a"))

# Invertir mayúsculas y minúscilas
print(text.swapcase())

print(text.startswith("Ella"))
print(text.endswith("Java"))

print(text.replace("Python", "JavaScript"))


text_2 = "este es un título"
print("\ntext_2")
print(text_2)
print(text_2.capitalize())

print(text_2.isdigit())  # False
print("398".isdigit())  # True
