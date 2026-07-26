from pathlib import Path

file = Path("student.json")

file.touch()

print(file.exists())