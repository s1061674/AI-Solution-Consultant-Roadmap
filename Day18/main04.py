from pathlib import Path

folder = Path("data")
folder.mkdir(parents=True,exist_ok=True)

file = Path("data/student.json")

file.touch()

print(file.exists())