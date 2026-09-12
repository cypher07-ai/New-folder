n = int(input())
cleaning_plans = []

for i in range(n):
    x ,y = map(int, input().split())
    cleaning_plans.append((x, y))

cleaning_plans = tuple(cleaning_plans)
total_x = 0
total_y = 0

for x , y in cleaning_plans:
    total_x += x
    total_y += y
print("HD = ", total_x)
print("VD = ", total_y)