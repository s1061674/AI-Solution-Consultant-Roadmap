numbers = [1, 2, 3, 4, 5, 6]
result = [x ** 2 if x % 2 == 0 else x for x in numbers]
print(result)