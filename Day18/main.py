from pathlib import Path

folder = Path("test_folder")

folder.mkdir(
    exist_ok=True
)

print(folder.exists())

print(folder.resolve())