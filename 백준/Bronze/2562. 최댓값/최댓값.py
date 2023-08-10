list = []
for i in range(9):
    a = int(input())
    list.append(a)
maxV = list[0]
maxI = 0
for i in range(len(list)):
    if list[i] > maxV:
        maxV = list[i]
        maxI = i
print(maxV)
print(maxI+1)