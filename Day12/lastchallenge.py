with open("my_note.txt", "a") as file:
    file.write("\nI love Python")

with open("my_note.txt", "r") as file:
    print(file.read())
    