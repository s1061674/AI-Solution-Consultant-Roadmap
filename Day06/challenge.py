#要求：使用 Dictionary,List,for,append(),f-string
player ={
    "姓名": "HCK",
    "年齡": 27,
    "城市": "高雄",
}
games =[]
games.append("EFT")
games.append("ARC")
games.append("VAL")

print("=" *20 +"玩家資料"+ "=" *20)
print()
for key, Value in player.items():
    print(key, Value)
print("最喜歡玩的遊戲: ")
print()
for i in range(len(games)):
    print(f"{i+1}.{games[i]}")
