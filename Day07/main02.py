student = {
            "姓名": "HCK",
            "年齡": 27,
            "城市": "高雄"
        }  
while True:
    try:
        key = input("請輸入要查詢的資料：")
        value = student[key]
    except KeyError:
        print("查無此資料")
    else:
        print(f"{key}: {value}")
        break