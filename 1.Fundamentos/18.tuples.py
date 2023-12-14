# Una tupla es una estructura de datos en Python que
# permite almacenar múltiples elementos de diferentes
# tipos en una secuencia ordenada. A diferencia de las
# listas, las tuplas son inmutables, lo que significa
# que no se pueden modificar una vez creadas.

numbers = (1, 2, 3, 4)
strings = ("pruebas", "algo", "otra cosa", "algo")

print(numbers)
print("0 =>", numbers[0])
print("-1 =>", numbers[-1])
print(type(numbers))

print(strings)
print("0 =>", strings[0])
print(type(strings))

# Buscar el indice de un elemento
print("Index => ", strings.index("pruebas"))

# Contar la cantidad de repeticiones de un elemento
print(strings.count("algo"))

# Converir una tupla en una lista
my_list = list(strings)
print(my_list)
print(type(my_list))

# Convertir una lista en una tupla
my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))
