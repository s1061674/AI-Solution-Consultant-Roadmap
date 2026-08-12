class User:
    pass

class Staff(User):
    pass

class Admin(Staff):
    pass

user = Admin()

if isinstance(user, Admin):
    print("Admin access")
elif isinstance(user, Staff):
    print("Staff access")
elif isinstance(user, User):
    print("User access")
else:
    print("Access denied")