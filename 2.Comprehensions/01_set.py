# Los sets en Python son una estructura de datos que
# almacena una colección de elementos únicos y desordenados.
# Esto significa que no puede haber elementos duplicados en
# un set y no se mantiene un orden específico de los elementos.
#
# Los sets son útiles cuando necesitamos almacenar elementos
# sin importar su orden y cuando queremos asegurarnos de que
# no haya duplicados
set_countries = {"COL", "USA", "ESP", "FRA", "COL", "ESP"}
print(set_countries)  # {'COL', 'ESP', 'FRA', 'USA'}
print(type(set_countries))

set_numbers = {1, 2, 6, 6, 6}
print(set_numbers)  # {1, 2, 6}

set_types = {1, "hola mundo", False, False, 12, 20.99}
print(set_types)  # {False, 1, 12, 20.99, 'hola mundo'}

# Convierte un string en un set
set_from_string = set("hola mundo")
print(set_from_string)  # {'h', ' ', 'o', 'l', 'a', 'u', 'n', 'd', 'm'}

# Convierte una tupla en un set
set_from_tuples = set(("manzana", "pera", "uva", "pera"))
print(set_from_tuples)  # {'manzana', 'pera', 'uva'}

# Convierte una lista en un set
set_numbers = set([1, 2, 3, 1, 2, 3, 4])
print(set_numbers)  # {1, 2, 3, 4}
unique_numbers = list(set_numbers)
print(unique_numbers)  # [1, 2, 3, 4]
