word = input().upper()  # zZa > ZZA
uniqueWord = list(set(word))  # A, Z
#print(uniqueWord)
cnt = 0
lst = []
for i in uniqueWord:
    cnt = word.count(i)
    lst.append(cnt)
# print(lst)
# print(lst.index(max(lst)))

if lst.count(max(lst)) > 1:
    print('?')
else:
    maxIndex = lst.index(max(lst))
    print(uniqueWord[maxIndex])