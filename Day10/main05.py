def shipping(price):
    if price >=1000:
        return (0)
    else:
        return (60)
price = (int(input("請輸入消費金額: ")))

print(f"商品金額: {price}")
fee = shipping(price)
print(f"運費: {shipping(price)}")
total = price + fee
print(f"總金額: {total}")