products = [
    {"name": "Mouse", "price": 500},
    {"name": "Keyboard", "price": 2000},
    {"name": "Monitor", "price": 8000},
    {"name": "USB", "price": 300},
    {"name": "Headset", "price": 1500}
]

result = [product["name"] for product in products if product["price"] >= 1000]
print(result)