items = [
    {"product": "apple", "price": 10},
    {"product": "banana", "price": 5},
    {"product": "cherry", "price": 15},
]

print("items:", items)

prices = list(map(lambda item: item["price"], items))

print("prices:", prices)


items_with_tax = list(map(lambda item: {**item, "taxes": item["price"] * 0.16}, items))

print("items_with_tax:", items_with_tax)
print("items:", items)
