list = []
for _ in range(28):
    a = int(input())
    list.append(a)
list.sort()
count = 1
for i in list:
    while i > count:
        print(count)
        count += 1
    count += 1
while count <= 30:
    print(count)
    count += 1