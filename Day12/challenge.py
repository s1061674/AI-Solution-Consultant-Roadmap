file = open("my_note.txt", "w")

file.write("My name is HCK\nI am learning Python\nDay12")

file.close()

file = open("my_note.txt", "r")

content = file.read()

print(content)

file.close()


