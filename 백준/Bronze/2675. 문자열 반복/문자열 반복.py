t = int(input())
p = []
for i in range(t):
    r, s = input().split()
    r = int(r)
    for i in s:
        p.append(i*r)
    print(*p, sep='')
    p = []