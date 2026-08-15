names = ["Amy", "Tom", "Jack", "Bob"]
scores = [85, 60, 90, 55]

for index, (names, scores) in enumerate(zip(names, scores), start = 1):
    print(f"{index}. {names} scored {scores}")