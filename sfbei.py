n = int(input())

rainfall_data = tuple(tuple(map(int, input().split())) for _ in range(n))

year = int(input())

selected_year = rainfall_data[year - 1]
average = sum(selected_year) / len(selected_year)

print(round(average, 2))