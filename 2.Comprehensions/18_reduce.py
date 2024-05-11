import functools

numbers = [100, 20, 45, 98, 2, 41]

# La función lambda toma dos argumentos, el primero es el acumulador y el segundo es el elemento actual
# Counter es el acumulador y item es el elemento actual
sum_numbers = functools.reduce(lambda counter, item: counter + item, numbers)

print("sum_numbers: ", sum_numbers)
