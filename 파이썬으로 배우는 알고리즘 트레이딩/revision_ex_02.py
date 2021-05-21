'''
제어문: for
'''
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print("%s " % i, end='')
print()

for i in range(0, 11):  # range 객체를 그대로 쓰는 것이 메모리상 효율적
    print("%s " % i, end='')
print()

for i in list(range(0, 11)):
    print("%s " % i, end='')
print()

interest_stocks = ["Naver", "Samsung", "SK Hynix"]  # list
for company in interest_stocks:
    print("%s: Buy 10" % company)

interest_stocks = ("Naver", "Samsung", "SK Hynix")  # 튜플
for company in interest_stocks:
    print("%s: Buy 10" % company)

interest_stocks = {"Naver": 10, "Samsung": 5, "SK Hynix": 30}   # 딕셔너리
for company, stock_num in interest_stocks.items():
    print("%s: Buy %s" % (company, stock_num))

while i <= 10:
    print(i)
    i = i+1
