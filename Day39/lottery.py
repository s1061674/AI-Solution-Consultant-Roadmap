import random
def draw_winners(players, count):
   result = random.sample(players, count)
   return result

if __name__ == "__main__":
   players = ["Amy", "Tom", "Jack", "Bob", "Kevin"]
   result = draw_winners(players, 2)
   print(result)
