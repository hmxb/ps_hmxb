words = input().upper()
uniqueWords = list(set(words))
cntList = []
for i in uniqueWords:
    cnt = words.count(i)
    cntList.append(cnt)
if cntList.count(max(cntList)) > 1:
    print('?')
else:
    maxIndex = cntList.index(max(cntList))
    print(uniqueWords[maxIndex])