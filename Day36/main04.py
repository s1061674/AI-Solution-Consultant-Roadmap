students = [
    {"name": "Amy", "score": 85},
    {"name": "Tom", "score": 92},
    {"name": "Jack", "score": 78},
    {"name": "Bob", "score": 88}
]


result = sorted(students, key=lambda student: student["score"], 
                 reverse=True)
result = list(map(lambda student: student["name"], result))


print(result)