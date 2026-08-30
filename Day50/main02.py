from collections import defaultdict

students = [
    ("Python", "Arthur"),
    ("AI", "Amy"),
    ("Python", "Bob"),
    ("Web", "Jack"),
    ("AI", "Alice"),
    ("Python", "Tom")
]

groups = defaultdict(list)

for course, name in students:
    groups[course].append(name)

for course, names in groups.items():
    print(f"{course}: {names}")