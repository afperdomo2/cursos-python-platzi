numbers = []
for element in range(1, 11):
    numbers.append(element * 2)

print("numbers:", numbers)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# List comprehension
numbers_2 = [element for element in range(1, 11)]
print("numbers_2:", numbers_2)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers_3 = [element * 2 for element in range(1, 11)]
print("numbers_3:", numbers_3)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

pairs = []
for i in range(1, 11):
    if i % 2 == 0:
        pairs.append(i * 2)

print("pairs:", pairs)  # [4, 8, 12, 16, 20]

pairs_2 = [i * 2 for i in range(1, 11) if i % 2 == 0]
print("pairs_2:", pairs_2)  # [4, 8, 12, 16, 20]
