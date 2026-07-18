def ticket(age):
    if age >= 65:
        return ("150元")
    elif age >= 12:
        return ("250元")
    else:
        return ("100元")
age = int(input("請輸入年齡: "))
print(f"票價: {ticket(age)}")