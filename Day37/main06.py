products = {
    "Mouse": 500,
    "Keyboard": 2000,
    "Monitor": 8000,
    "USB": 300,
    "Headset": 1500
}

result = {name.upper(): price * 0.8 for name, price in products.items() if price >= 1000}

print(result)