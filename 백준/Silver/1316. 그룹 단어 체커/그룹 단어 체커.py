N = int(input())
groupList = []
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for _ in range(N):
    words = list(input())

    # 그룹단어일 시 넣어서 len

    # 그룹단어가 안될 경우
    # 중복이 끝났을때 또 나오는경우
    
    # 중복을 제거
    for i in range(len(words)-1, 0, -1):
        if words[i] == words[i-1]:
            words.pop(i)
    # print(words)

    groupWords = False
    # 중복을 제거한 단어를 알파벳과 비교하여 없애고
    # 없앤 알파벳이 또 나오면 그룹단어가 아님
    for i in words:
        if i in alpha:
            alpha.remove(i)
            groupWords = True
        else:
            groupWords = False
            break
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    # print(groupWords)
    if groupWords:
        groupList.append(words)
        
#print(groupList)
print(len(groupList))