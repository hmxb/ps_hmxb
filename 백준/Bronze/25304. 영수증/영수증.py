total = int(input())
count = int(input())
money = 0
for i in range(count):
    a, b = map(int, input().split())
    money += a*b
if(total == money):
    print("Yes")
else:
    print("No")