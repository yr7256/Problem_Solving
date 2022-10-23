nums = [False, False]+[True]*(102)
plist = []
for i in range(2, 104):
    if nums[i]:
        plist.append(i)
        for j in range(2*i, 104, i):
            nums[j] = False
special = []
for i in range(len(plist)-1):
    special.append(plist[i]*plist[i+1])
N = int(input())
for i in special:
    if i > N:
        print(i)
        break
