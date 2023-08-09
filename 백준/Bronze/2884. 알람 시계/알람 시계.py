a, b = map(int, input().split())
if a==0 and b<45:
    print(23, 15+b)
elif b<45:
    print(a-1, 15+b)
elif b>=45:
    print(a, b-45)