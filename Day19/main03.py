from pathlib import Path
import json

file = Path("data/student.json")

data = json.loads(file.read_text())

print(type(data))