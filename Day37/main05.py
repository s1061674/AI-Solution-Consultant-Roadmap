scores = {
    "Amy": 85,
    "Tom": 60,
    "Jack": 90,
    "Bob": 55
}

result = {name: "Pass" if score >= 60 else "Fail" for name, score in scores.items()}

print(result)
