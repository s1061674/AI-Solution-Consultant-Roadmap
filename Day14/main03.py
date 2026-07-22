try:
    age = int(input("請輸入年齡："))

except ValueError:
    print("請輸入數字！")

else:
    print(f"你的年齡是 {age}")

finally:
    print("程式結束")