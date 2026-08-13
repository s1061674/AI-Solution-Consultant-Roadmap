students = [
    {"name": "Amy", "score": 60},
    {"name": "Tom", "score": 90},
    {"name": "Jack", "score": 75},
    {"name": "Bob", "score": 50},
    {"name": "Kevin", "score": 85}
]

result = filter(lambda student: student["score"] >= 70, students)

result = sorted(result, key=lambda student: student["score"], reverse=True)

result = list(map(lambda student: student["name"], result))

print(result)