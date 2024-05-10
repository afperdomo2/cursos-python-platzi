items = [
    {"product": "apple", "price": 10},
    {"product": "banana", "price": 5},
    {"product": "cherry", "price": 15},
]

print("items:", items)

prices = list(map(lambda item: item["price"], items))


def add_taxes(item):
    return {**item, "taxes": item["price"] * 0.16}


items_with_taxes = list(map(add_taxes, items))

print("items_with_taxes:", items_with_taxes)
print("items:", items)
