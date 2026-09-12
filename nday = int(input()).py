n1 = int(input())
weekday_stock = []
for i in range(n1):
    weekday_stock.append(int(input()))
weekday_stock = tuple(weekday_stock)


n2 = int(input())
weekend_stock = []
for i in range(n2):
    weekend_stock.append(int(input()))
weekend_stock = tuple(weekend_stock)

merge = weekday_stock + weekend_stock
total_quant = sum(merge)
a = len(merge)
reorder = merge*2

print(merge)
print(total_quant)
print(a)
print(reorder)