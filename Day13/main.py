import json

student = {
    "name": "Tom",
    "age": 18,
    "score": 100
}

with open("student.json", "w") as file:
    json.dump(student, file)

print("完成")