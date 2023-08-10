Lst = []
for _ in range(10):
    a = int(input())
    Lst.append(a)
lst=[]
for i in Lst:
    b = i%42
    lst.append(b)
setList = list(set(lst))
print(len(setList))