students = [
    {"name": "HCK", "score": 99},
    {"name": "Amy", "score": 66},
    {"name": "Kevin", "score": 90}
]

names = [
    f"{student["name"]}:{student["score"]}"
    for student in students
]

print(names) 