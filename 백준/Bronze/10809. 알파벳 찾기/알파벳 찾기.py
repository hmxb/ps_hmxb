str = list(input())
lst= ['a', 'b', 'c', 'd' ,'e', 'f', 'g', 'h', 'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lstt = []

for i in lst:
    if i in str:
        lstt.append(str.index(i))
    else:
        lstt.append(-1)
print(*lstt)