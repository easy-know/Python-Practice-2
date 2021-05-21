'''
제어문: Boolean, If, If~else, if ~ elif ~else, for
'''
wikibooks_cur_price = 11000
# IF문
if wikibooks_cur_price >= 10000:
    print("Buy 10")

# IF~ELSE 문
if wikibooks_cur_price >= 12000:
    print("Buy 10")
else:
    print("Holding")

# if ~ elif ~ else
price = 7000
if price < 1000:
    bid = 1
elif price >= 1000 and price < 5000:
    bid = 5
elif price >= 5000 and price < 10000:
    bid = 10
elif price >= 10000 and price < 50000:
    bid = 50
elif price >= 50000 and price < 100000:
    bid = 100
elif price >= 100000 and price < 500000:
    bid = 500
elif price >= 500000:
    bid = 1000

print(bid)
