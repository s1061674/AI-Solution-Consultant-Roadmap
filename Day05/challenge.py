games = []
count = 1
print("請輸入三個喜歡的遊戲")
for i in range(3):
    games.append(input(f"請輸入第{count}個喜歡的遊戲: "))
    count += 1
print("你最喜歡的遊戲")
print()
for game in games:
    print(game)
