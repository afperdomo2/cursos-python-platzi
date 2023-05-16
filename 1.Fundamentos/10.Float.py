# Comparación de flotantes

x = 3.3
print("x:", x)  # 3.3

y = 1.1 + 2.2
print("y:", y)  # 3.3000000000000003

print(x == y)  # False, la precisión es diferente, "3.3" != "3.3000000000000003"


y_str = format(y, ".2g")
print("y_str:", y_str)  # "3.3"

print(str(x) == y_str)  # "3.3" == "3.3", True, misma precisión


print("\n***********")


# Forma matemática de comparar x con y, definiendo un nivel
# de tolerancia de decimales
tolerance = 0.00001
diff = abs(x - y)
print("diff:", diff)
print(diff < tolerance)  # True


print("\n***********")


# Otra forma, redondeando los valores
x = 3.3
y = round(y, 1)

print(x == y)  # True
