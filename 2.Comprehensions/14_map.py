numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, numbers))

print(squared)

numbers_1 = [1, 2, 3, 4, 5]
numbers_2 = [6, 7, 8, 9, 10]

result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print("result:", result)
