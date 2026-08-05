def info(name, score):
    print(f"{name}: {score}")

student = {"name": "Amy", "score": 88}

info(**student)