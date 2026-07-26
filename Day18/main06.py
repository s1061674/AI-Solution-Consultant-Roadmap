from pathlib import Path

file = Path("data/note.txt")

file.write_text("""我是 HCK
今天開始學 Pathlib
我要成為 AI Solution Consultant""")

print(file.read_text())