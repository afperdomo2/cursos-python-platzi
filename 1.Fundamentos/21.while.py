if True:
    print("Se cumple la condición")

counter = 0
print("counter:", counter)
while counter < 3:
    print(counter)
    counter += 1

x = 0
print("x:", x)
while x < 10:
    print(x)
    if x == 5:
        break  # Rompe el ciclo
    x += 1

y = 0
print("y:", y)
while y < 10:
    y += 1
    if y < 7:
        continue  # Salta a la siguiente iteración
    print(y)
