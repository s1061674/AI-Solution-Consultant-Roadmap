names = ["Amy", "Alexander", "Tom", "Jack", "Bob"]

result = {name: len(name) for name in names if len(name) > 3}

print(result)