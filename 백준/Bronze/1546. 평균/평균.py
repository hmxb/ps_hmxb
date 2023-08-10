n = int(input())
lst = list(map(int, input().split()))
maxS = max(lst)
Lst = []
for i in lst:
    Lst.append(i/maxS*100)
avgS = sum(Lst)/n
print(avgS)