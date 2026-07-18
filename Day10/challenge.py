def pass_or_fail(score):
    if score >= 60:
        return ("及格")
    else:
        return ("不及格")
score = int(input("請輸入分數: "))
print(f"結果: {pass_or_fail(score)}")