numbers = [5, 12, 7, 20, 3, 15, 8]

result = list(
        map(
        lambda x: x * 3,
        filter(lambda x: x >= 10, numbers)
    )   
)

print(result)