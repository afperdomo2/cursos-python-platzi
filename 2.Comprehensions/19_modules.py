import sys
import re
import time
import collections

# sys.path es una lista de directorios donde Python busca módulos
print(sys.path)


texto = "Mi número de teléfono es 123-456-7890, el código del país es +57"
# re.findall busca todas las ocurrencias de un patrón en un texto
phone_numbers = re.findall("[0-9]+", texto)
print(phone_numbers)

timestamp = time.time()
print("timestamp:", timestamp)

local_time = time.localtime()
local = time.asctime(local_time)
print("local time:", local)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# collections.Counter cuenta las ocurrencias de los elementos de una lista
counter = collections.Counter(numbers)
print("counter:", counter)
