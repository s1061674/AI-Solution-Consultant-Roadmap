products = ["Mouse", "Keyboard", "Monitor", "USB", "Headset"]
prices = [500, 2000, 8000, 300, 1500]

result = [
f"{products}: ${prices}"
for products, prices in zip(products, prices)
if prices >= 1000
]
result = [
    f"{index}. {item}"
    for index, item in enumerate(result, start = 1)
]
print(result)
