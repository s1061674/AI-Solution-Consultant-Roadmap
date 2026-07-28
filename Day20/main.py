from pathlib import Path
import json

BASE_DIR = Path(__file__).parent

file = BASE_DIR / "data" / "students.json"

students = json.loads(file.read_text())


def show_students():
    print("===== Student List =====")

    for index, student in enumerate(students, start=1):
        print(f"{index}. {student["name"]} - {student["score"]}分")
def add_student():
    name = input("請輸入姓名：")

    while True:
        try:
            score = int(input("請輸入分數："))
            break

        except ValueError:
            print("請輸入數字！")
            
    students.append({
        "name": name,
        "score": score
    })

    file.write_text(json.dumps(students, indent=4))
    print("新增成功！")
def menu():
    while True:
        print("===== Student Manager =====")
        print("1. 顯示學生 \n2. 新增學生 \n3. 離開")

        choice =input("請輸入選項:")

        if choice == "1":
            show_students()
        elif choice == "2":
            show_students()
            add_student()
        elif choice == "3":
            print("Bye!")
            break
        else:
            print("請輸入正確選項！")
menu()
