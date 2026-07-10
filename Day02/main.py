print("=" *40)
print("AI Bootcamp Day02")
print("=" *40)

name = input("請輸入你的名字: ")
age = int(input("請輸入你的年齡: "))

print()


print(f"你好 {name}！")
print(f"你今年 {age} 歲。")
print(f"明年就 {age + 1} 歲了!")
print(f"5年後你就是 {age + 5} 歲了!")

print("=" *40)

print()

print("=" * 20 + " 個人資料 " + "=" * 20)
print(f"姓名\t{name}")
print(f"年齡\t{age}")
print("目標\tAI Solution Consultant")


print()
print("=" *20 + " 年齡判斷 " + "=" *20)

age = int(input("請輸入你的年齡: "))

if age >= 18:
    print("🎉 你已經成年了!")
else:
    print("😢 你還未成年!")

print()
print("=" *20 + " 年齡判斷 " + "=" *20)
age = int(input("請輸入你的年齡: "))

if age < 0:
    print("❌ 請輸入有效的年齡!")
elif age <= 12:
    print("👶 小朋友")
elif age <= 17:
    print("🧑 青少年")
elif age <= 64:
    print("成年人")
else:
    print("👴 長者")