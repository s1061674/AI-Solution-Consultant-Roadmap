import json

with open("student.json", "r") as file:
    student = json.load(file)

try:
    new_score = int(input("請輸入新的分數："))

except ValueError:
    print("請輸入數字！")

else:
    student["score"] = new_score

    with open("student.json", "w") as file:
        json.dump(student, file)

    print("更新完成！")