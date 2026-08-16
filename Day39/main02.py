import random

players = ["Amy", "Tom", "Jack", "Bob", "Kevin", "John"]

result = random.sample(players, 3)

print("Winners:")

for index, winner in enumerate(result, start = 1):
    
    print(f"{index}. {winner}") 