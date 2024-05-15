try:
    print(0 / 0)

    assert 1 != 1, "Uno no es igual a uno"

    age = 10
    if age < 18:
        raise Exception("Menor de edad")

# Capturar varios errores
except ZeroDivisionError as error:
    print("\nerror:", error)
    print("⛔ No se puede dividir por cero")
except AssertionError as error:
    print("\nerror:", error)
    print("⛔ La afirmación no es verdadera")
except Exception as error:
    print("\nerror:", error)
    print("⛔ No pueden ingresar a menores de edad")

# try:
#     assert 1 != 1, "Uno no es igual a uno"
# except AssertionError as error:
#     print("\nerror:", error)
#     print("⛔ La afirmación no es verdadera")


# try:
#     age = 10
#     if age < 18:
#         raise Exception("Menor de edad")
# except Exception as error:
#     print("\nerror:", error)
#     print("⛔ No pueden ingresar a menores de edad")


print("\n👋 Hola mundo")
