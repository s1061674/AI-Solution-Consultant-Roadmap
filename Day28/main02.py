def total(*numbers):
    result = 0

    for number in numbers:
        result += number

    print(result)

total(5, 10, 15, 20)
