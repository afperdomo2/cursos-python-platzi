# Higher order functions
#
# Una función de orden superior es una función que acepta otras
# funciones como argumentos o devuelve una función como resultado.


# 1. Versión con funciones
def increment(x):
    return x + 1


def high_order_function(func, x):
    return func(x) + x


result = high_order_function(increment, 2)

print(result)  # 5


# 2. Versión con lambda
increment_v2 = lambda x: x + 1  # noqa: E731
high_order_function_v2 = lambda func, x: func(x) + x  # noqa: E731
result_v2 = high_order_function_v2(increment_v2, 2)
print(result_v2)  # 5


# Enviando una lambda directamente como argumento
result_v3 = high_order_function_v2(lambda x: x * 5, 2)
print(result_v3)  # 12
