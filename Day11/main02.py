import math

number = int(input("請輸入一個數字："))

print(f"平方根：{math.sqrt(number)}")
print(f"平方：{(number ** 2)}")
print(f"無條件進位：{math.ceil(number / 3)}")
print(f"無條件捨去：{math.floor(number / 3)}")