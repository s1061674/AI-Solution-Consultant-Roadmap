def even_numbers(max_value):
    start = 2
    while start <= max_value:
        yield start
        start += 2

for number in even_numbers(10):
    print(number)