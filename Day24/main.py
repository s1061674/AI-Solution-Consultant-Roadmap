def create_student(name, score):
    return {
        "name": name,
        "score": score
    }
    

student = create_student("HCK", 99)
student1 = create_student("Amy", 80)
student2 = create_student("Kevin", 95)
print(student)
print(student1)
print(student2)
