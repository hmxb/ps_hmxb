lst = list(map(int, input().split()))
lst1 = [1,1,2,2,2,8]
lst2 = []
for i in range(len(lst)):
    lst2.append(lst1[i]-lst[i])
print(*lst2)