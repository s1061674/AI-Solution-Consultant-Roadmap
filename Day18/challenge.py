from pathlib import Path

folder = Path("logs/")
folder.mkdir(parents = True, exist_ok = True)

file = folder / "today.txt"
file.write_text("""Python Day18 
Pathlib 練習完成""")
print(file.read_text())