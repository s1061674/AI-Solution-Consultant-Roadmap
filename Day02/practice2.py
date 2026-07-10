print("=" * 20)
print("     登入系統")
print("=" * 20)

username = input("請輸入帳號: ")
password = input("請輸入密碼: ")

if username == "admin" and password == "1234":
    print("登入成功")
else:
    print("登入失敗")
