print("=" * 20)
print("BMI 計算機")
print("=" * 20)
print()

name = input("請輸入姓名: ")
height = float(input("請輸入身高(公分): "))
weight = float(input("請輸入體重(公斤): "))
bmi = weight / ((height / 100) * (height / 100) )

print("=" * 20)
print(f"{name} 的 BMI 計算結果")
print("=" * 20)
print(f"姓名: {name}")
print(f"身高: {height:.1f} 公分")
print(f"體重: {weight:.1f} 公斤")
print(f"BMI: {bmi:.2f}")
if bmi < 18.5:
    print("體重過輕")
    print("建議: 多吃高熱量食物，並增加運動量")
elif bmi < 24:
    print("體重正常")
    print("建議: 維持現有生活習慣，並持續運動")
elif bmi < 27:
    print("體重過重")
    print("建議: 減少高熱量食物攝取，並增加運動量")
else:
    print("輕度肥胖")
    print("建議: 減少高熱量食物攝取，並增加運動量")
print("=" * 20)