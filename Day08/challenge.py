import random
games = []

print("輸入五個喜歡的遊戲")

for i in range(5):
    games.append(input(f"請輸入第{i+1}個遊戲: "))
random.shuffle(games)

print()

print("=" *20 +"今日推薦"+ "=" *20)

print()

count = 1
for game in games:
    print(f"{count}.{game}")
    count += 1  

print()

print("今日精選:")
print(random.choice(games))