croList = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
str = input()
for cro in croList:
    str = str.replace(cro, 'a')
print(len(str))