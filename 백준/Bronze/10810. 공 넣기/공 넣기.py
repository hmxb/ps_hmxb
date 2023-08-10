N, M = map(int, input().split())
list = [0]*N
while M > 0:
    i, j, k = map(int, input().split())
    list[i-1:j] = [k]*(j-i+1)
    M -= 1
for i in range(N):
    print(list[i], end = ' ')