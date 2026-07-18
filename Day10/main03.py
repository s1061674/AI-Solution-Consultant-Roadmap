def discount(price):
    return (price * 0.8)
price = int(input("請輸入商品價格:"))
print(f"折扣後價格: {discount(price)}")