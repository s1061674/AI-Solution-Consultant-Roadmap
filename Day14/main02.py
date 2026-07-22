try:
    number = int(input("請輸入一個數字:"))

except ValueError:
    print("輸入錯誤!")

else:
    print(f"你輸入的是{number}")
    