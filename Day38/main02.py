names = ["Amy", "Tom", "Jack", "Bob"]
scores = [85, 60, 90, 55]

for names, scores in zip(names, scores):
    print(f"{names} scored {scores}")