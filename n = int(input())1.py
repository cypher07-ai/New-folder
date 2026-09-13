n = int(input())
result = {}

for i in range(n):
    parts = input().split()
    cid = int(parts[0])
    amount = list(map(int,parts[1:]))
    total = sum(amount)
    maxi = max(amount)
    result[cid] = [total , maxi]
print(result)