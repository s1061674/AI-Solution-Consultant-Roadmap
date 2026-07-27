from pathlib import Path
import json

file = Path("data/student.json")

data = json.loads(file.read_text())

data["city"] = "Kaohsiung"

data["vip"] = True

file.write_text(json.dumps(data, indent=4))

print(file.read_text())