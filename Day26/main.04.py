students = [
    ("HCK", 99),
    ("Amy", 66),
    ("Kevin", 90)
]

result = sorted(students, key=lambda x: x[1], reverse=True)
print(result)