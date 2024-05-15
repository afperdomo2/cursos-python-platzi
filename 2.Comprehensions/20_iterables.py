# Comprehensions: Iterables
# Iterables: Son objetos que se pueden recorrer uno a uno, como una lista, un diccionario, una tupla, un string, etc.

for i in range(1, 10):
    print(i)

# iter() es una función que nos permite convertir un iterable en un iterador
my_iter = iter(range(1, 4))  # Este es un iterador
print(my_iter)

# Next() es una función que nos permite obtener el siguiente elemento de un iterador
print(next(my_iter))  # 1
print(next(my_iter))  # 2
print(next(my_iter))  # 3
print(next(my_iter))  # Error: StopIteration
