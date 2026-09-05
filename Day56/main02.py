names = ["Amy", "Alexander", "Bob", "Kevin", "Tom", "Michael"]

result = list(
    map(
        lambda x: x.upper(),
        filter(lambda x: len(x) >= 5, names)
    )
)   

print(result)