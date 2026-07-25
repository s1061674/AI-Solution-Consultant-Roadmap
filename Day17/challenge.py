students = [
    {"name": "Tom", "score": 80},
    {"name": "Amy", "score": 95},
    {"name": "John", "score": 50},
    {"name": "Kevin", "score": 88},
]

result = { student["name"]:"Pass" if student["score"] >= 60 else "Fail"
            for student in students
        }   
print(result)