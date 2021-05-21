'''
dict: {}
'''
cur_price = {}
print(type(cur_price))

cur_price['daeshin'] = 30000
print(cur_price)

cur_price['Daum KAKAO'] = 80000
print(cur_price)

print(len(cur_price))
print(cur_price['daeshin'])
print(cur_price['Daum KAKAO'])

del cur_price['daeshin']
print(cur_price)

print(cur_price.keys())

stock_list = list(cur_price.keys())
print(stock_list)

price_list = list(cur_price.values())
print(price_list)

print('Samsung' in cur_price.keys())
