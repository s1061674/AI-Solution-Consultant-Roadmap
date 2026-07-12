answer = 7
count = 0

while True:
    guess = int(input("請猜數字: "))
    count += 1
    
    if guess == answer:
        print("恭喜猜對！")  
        print(f"你總共猜了 {count} 次!")
        break

    elif count == 5:
        print(f"遊戲結束!\n答案是 {answer}")
        break

    elif guess < answer:
        print("猜太小了")

    else:
        print("猜太大了")
    