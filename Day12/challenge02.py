with open("my_note.txt", "w") as file:

    file.write("My name is HCK\nI am learning Python\nDay12")

with open("my_note.txt", "r") as file:

    content = file.read()

    print(content)



