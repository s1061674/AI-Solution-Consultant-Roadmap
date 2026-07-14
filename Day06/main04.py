student = {
    "姓名": "HCK",
    "年齡": 27,
    "城市": "高雄"
}
#第一種
for key in student:
    print(key, student[key])
#第二種
for key, value in student.items():
    print(key, value)

print(student.keys())
print(student.values())
print(student.items())