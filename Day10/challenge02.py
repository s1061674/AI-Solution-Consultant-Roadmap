def discount(price):
    return (price * 0.8)
def show(price):
    discount(price)
price = int(input("請輸入商品價格: "))
print(f"原價: {price} 元")
print(f"折扣後: {discount(price):.0f} 元")