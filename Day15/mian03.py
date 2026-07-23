def calculate_price(price, discount=0):

    return (price-price *discount/100)

print (f"{calculate_price(100):.0f}")
print(f"{calculate_price(100, 20):.0f}")