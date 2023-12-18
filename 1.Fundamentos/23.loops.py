matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("matriz:", matriz)
print(matriz[0])  # [1, 2, 3]
print(matriz[0][2])  # 3

print("Recorriendo una matriz")
for row in matriz:
    print(row)
    for column in row:
        print(column)
