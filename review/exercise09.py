prices = [15.0, 230.0, 8.5, 99.9, 450.0, 32.0, 175.0]

price_up50 = [p for p in prices if p > 50]
print(price_up50)

price_discount = [d - (d * 0.10) for d in prices]
print(price_discount)