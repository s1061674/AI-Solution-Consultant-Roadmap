def person(name, age):
    if age >= 18:
        return (f"{name} 已成年")
    else:
        return (f"{name} 未成年")
    
name = input("請輸入姓名: ")
age = int(input(f"請輸入年齡: "))

print(person(name, age))

