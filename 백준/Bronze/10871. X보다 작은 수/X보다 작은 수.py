n, x = map(int, input().split())
lst = list(map(int, input().split()))
Lst = []
for i in lst:
    if i < x:
        Lst.append(i)
for i in Lst:
    print(i, end =' ')