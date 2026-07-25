students = [
    {"name": "Tom", "score": 80},
    {"name": "Amy", "score": 95},
    {"name": "John", "score": 70},
    {"name": "Kevin", "score": 88}
]

result = sorted(students, key=lambda x: x["score"], reverse=True)

for student in result:

    print(student["name"],student["score"])