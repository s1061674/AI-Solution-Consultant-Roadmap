from pathlib import Path

file = Path("data/note.txt")

file.write_text("AI Solution Consultant")

print(file.exists())

print(file.read_text())