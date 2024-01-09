price = 100  # Global scope


def increment():
    price = 50  # Local scope
    price = price + 1
    print(price)


print(price)  # 100
increment()  # 51
