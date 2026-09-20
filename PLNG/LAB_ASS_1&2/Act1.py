#HILVANO, STEVEN REIGN S.
#BSCS 2-Y1-1  

exchange_rate = 0.85

for i in range(1, 7):
    usd_price = float(input(f"Enter price of product {i} in USD: "))
    euro_price = usd_price * exchange_rate

    print(f"Product {i}: €{euro_price:.2f}")