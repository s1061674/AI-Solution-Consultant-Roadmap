games = [ 
    "EFT",
    "ARC",
    "VAL",
    "PUBG",
    "APEX",
    "CS"
]
import random
random.shuffle(games)
print("今天推薦遊戲")
count = 1
for game in games:
    print(f"{count}.{game}")
    count += 1