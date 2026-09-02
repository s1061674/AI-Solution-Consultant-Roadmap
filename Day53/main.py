def countdown(start):
    while start > 0:
        yield start
        start -= 1

for number in countdown(5):
    print(number)