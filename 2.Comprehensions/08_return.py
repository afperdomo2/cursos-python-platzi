def sum_with_range(min, max):
    sum = 0
    for x in range(min, max):
        sum += x
    return sum


sum1 = sum_with_range(1, 5)
print(sum1)
sum2 = sum_with_range(1, 10)
print(sum2)
sum3 = sum_with_range(1, 100)
print(sum3)
total = sum1 + sum2 + sum3
print(total)
