import json

with open("student.json", "r") as file:
    student = json.load(file)

print(student["name"])
print(student["score"])


student["city"] = "Kaohsiung"
new_score = int(input("請輸入新的分數："))
student["score"] = new_score

with open("student.json", "w") as file:
    json.dump(student, file)

print("更新後的資料：")
print(f"姓名：{student['name']}")
print(f"年齡：{student['age']}")
print(f"分數：{student['score']}")
print(f"城市：{student['city']}")
print("更新完成！")