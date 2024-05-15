# print(0 / 0) # Error: ZeroDivisionError

# print(result) # NameError: name 'result' is not defined

suma = lambda a, b: a + b
assert suma(2, 2) == 4


age = 10
if age < 18:
    raise Exception("Menor de edad")
