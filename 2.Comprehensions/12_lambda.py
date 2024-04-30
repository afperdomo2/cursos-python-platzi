# Las funciones anónimas, también conocidas como funciones lambda,
# son funciones que se definen sin un nombre. En Python, se crean
# con la palabra clave lambda.


def increment(x):
    return x + 1


# Definir y llamar a la función lambda
(lambda x: x * 2)(3)
print((lambda x: x * 2)(10))  # 20

# Definir una función lambda y asignarla a una variable
increment_v2 = lambda x: x + 1  # noqa: E731
result = increment_v2(5)
print(result)  # 6


full_name = lambda first, last: f"Full name: {first.title()} {last.title()}"
print(full_name("guido", "van rossum"))  # Full name: Guido Van Rossum
