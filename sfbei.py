n = int(input())
ids = tuple(map(int,input().split()))
ids = list(ids)
x = int(input())
length=len(ids)
l1=[]
for i in range (length):
    if (i+1)%x!=0:
        l1.append(ids[i])
print(tuple(l1))