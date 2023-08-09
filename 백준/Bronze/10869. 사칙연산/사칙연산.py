a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
if(b == 0):
    print("0으로 몫을 구할 수 없습니다.")
else:
    print(a//b)
print(a%b)