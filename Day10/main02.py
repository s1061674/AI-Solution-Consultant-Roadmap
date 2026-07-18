def grade(score):
    if score >= 90:
        return ("A")
    elif score >= 80:
        return ("B")
    elif score >= 70:
        return ("C")
    elif score >= 60:
        return ("D")
    else :
        return ("F")
score = int(input(f"請輸入分數: "))
print(f"你的成績: {grade(score)}")