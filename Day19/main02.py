from pathlib import Path
import json

file = Path("data/student.json")

student = {
    "name": "HCK",
    "age": 27,
    "score": 100
}

json_text = json.dumps(student, indent=4)

file.write_text(json_text)
print(file.read_text())

data = json.loads(file.read_text())

print(data)
print(type(data))
print(data["name"])
print(data["score"])