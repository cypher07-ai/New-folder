n = int(input())
employees = []
for i in range(n):
    parts = input().split()
    employees.append((int(parts[0]), parts[1], parts[2], int(parts[3]), float(parts[4])))

for i in employees:
    yoe = i[3]
    sal = i[4]
    if yoe < 2:
        hike = 5
    elif yoe <= 5:
        hike = 10
    else:
        hike = 20
    new_salary = sal + (sal * hike / 100)
    print(f"{i[1]} {i[2]} {new_salary:.2f}")

    