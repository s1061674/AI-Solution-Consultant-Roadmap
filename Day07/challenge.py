player ={}
games = []

player["姓名"] = input("請輸入姓名:")

while True:    
    try:
        player["年齡"] = int(input("請輸入年齡:"))
    except ValueError:
        print("請輸入年齡:")
    else:
        break

player["城市"] = input("請輸入居住城市:")

print("請輸入三個喜歡的遊戲")

for i in range(3):
    games.append(input(f"{i+1}."))

print("=" *20 +"玩家資料"+ "=" *20)
print()
print(f"姓名: {player["姓名"]}")
print(f"年齡: {player["年齡"]}")
print(f"城市: {player["城市"]}")
print()
print("喜歡的遊戲: ")
for i in range(3):
    print(f"{i+1}.{games[i]}")
