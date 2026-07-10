print("=" * 20)
print("成績判斷系統")
print("=" * 20)
score =int(input("輸入你的成績: "))

if score > 100 or score < 0:
    print("輸入錯誤，請輸入0~100之間的數字")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("FAIL")
