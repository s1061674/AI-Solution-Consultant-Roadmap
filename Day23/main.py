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

    save_students()
    print("新增成功！")
def menu():
    while True:
        print("===== Student Manager =====")
        print("1. 顯示學生 \n2. 新增學生 " \
        "\n3. 修改學生 \n4. 刪除學生\n5. 搜尋學生\n6. 離開")

        choice =input("請輸入選項:")

        if choice == "1":
            show_students()
        elif choice == "2":
            show_students()
            add_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            search_student()
        elif choice == "6":
            print("Bye!")
            break
        
        else:
            print("請輸入正確選項！")

def update_student():
    show_students()
    index = get_student_index()

    new_score = get_score("請輸入新的分數:")

    students[index]["score"] = new_score
    save_students()
    print("修改成功！")
    show_students()

def delete_student():
    show_students()
    index = get_student_index()

    del students[index]
    save_students()
    print("刪除成功！")
    show_students()

def search_student():
    name = input("請輸入姓名:")

    found = False
    
    for student in students:
        if student["name"] == name:
            print("找到學生！")
            print(f"{student["name"]}-{student["score"]}分")
            found = True
            break
    if not found:
        print("找不到學生！") 

def get_student_index():
    while True:
        try:
            choice = int(input("請輸入學生編號："))

            if choice > len(students) or choice < 1:
                print("請輸入正確編號")
            else:
                return choice - 1

        except ValueError:
            print("請輸入數字！")

def save_students():
    file.write_text(json.dumps(students, indent=4))

def get_score(message):
    while True:
        try:
            score = int(input(message))
            return score
        except ValueError:
            print("請輸入數字！")

menu()