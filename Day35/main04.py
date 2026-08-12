class User:
    pass

class Admin(User):
    pass

class Guest(User):
    pass

user = Admin()

if isinstance(user, Admin):
    print("Admin access")
elif isinstance(user, User):
    print("User access")
else:
    print("Access denied")
    