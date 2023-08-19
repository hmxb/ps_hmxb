a = list(input())
b = 1
for i in range(len(a)//2):
    if a[i] != a[-(i+1)]:
        b = 0
        break
if b == 1:
    print(1)
else:
    print(0)