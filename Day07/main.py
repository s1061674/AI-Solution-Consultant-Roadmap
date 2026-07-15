while True:
    try:
        age = int(input("請輸入年齡： "))
    except ValueError:
        print("請重新輸入！")
    else:
        break
print(f"你的年齡是: {age}")