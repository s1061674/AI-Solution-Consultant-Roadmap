def bmi(weight, height):
    return weight / height ** 2

height = float(input("請輸入身高(cm):")) / 100
weight = float(input("請輸入體重(kg):"))

result = bmi(weight, height)
print(f"{result:.2f}")