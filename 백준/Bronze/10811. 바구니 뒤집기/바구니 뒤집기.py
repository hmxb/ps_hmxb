N, M = map(int, input().split())
lst = [i for i in range(1,N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    temp = lst[a-1:b]
    temp.reverse()
    lst[a-1:b] = temp
for i in range(N):
    print(lst[i], end =' ')