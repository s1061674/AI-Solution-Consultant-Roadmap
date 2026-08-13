products = [
    {"name": "Mouse", "price": 500},
    {"name": "Keyboard", "price": 2000},
    {"name": "Monitor", "price": 8000},
    {"name": "USB", "price": 300},
    {"name": "Headset", "price": 1500}
]

result = filter(lambda product: product["price"] >= 1000, products)

result = sorted(result, key=lambda product: product["price"], reverse=True)

result = map(lambda product: product["name"], result)

print(list(result))