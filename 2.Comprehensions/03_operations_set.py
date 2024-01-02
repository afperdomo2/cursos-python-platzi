set_a = {"COL", "MEX", "BOL"}
set_b = {"PE", "BOL"}

# 1. Union
set_c = set_a.union(set_b)
print(set_c)  # {'COL', 'MEX', 'BOL', 'PE'}

# Union usando el operador |
print(set_a | set_b)  # {'COL', 'MEX', 'BOL', 'PE'}

# 2. Intercection
set_c = set_a.intersection(set_b)
print(set_c)  # {'BOL'}
print(set_a & set_b)  # {'BOL'}

# 3. Difference
set_c = set_a.difference(set_b)
print(set_c)  # {'COL', 'MEX'}
print(set_a - set_b)  # {'COL', 'MEX'}

# 4. Symmetric difference
set_c = set_a.symmetric_difference(set_b)
print(set_c)  # {'COL', 'MEX', 'PE'}
print(set_a ^ set_b)  # {'COL', 'MEX', 'PE'}
