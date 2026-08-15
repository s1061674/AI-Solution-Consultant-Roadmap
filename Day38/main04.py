products = ["Mouse", "Keyboard", "Monitor", "Headset"]
prices = [500, 2000, 8000, 1500]

result = [
f"{products}: ${prices}"
for products, prices in zip(products, prices)
if prices >= 1500
]
print(result)