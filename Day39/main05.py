import lottery

players = ["Amy", "Tom", "Jack", "Bob", "Kevin", "JJ"]

result = lottery.draw_winners(players, 3)

print("Winners:")
for index, winner in enumerate(result, start = 1):
    print(f"{index}. {winner}")