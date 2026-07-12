answer = 7

while True:

    guess = int(input("請猜數字: "))

    if guess == answer:
        print("恭喜猜對！")  
        break
    elif guess < answer:
        print("猜太小了")
    else:
        print("猜太大了")
    