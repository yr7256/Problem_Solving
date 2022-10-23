from collections import deque
nums = [False, False]+[True]*(1003001)
plist = []
for i in range(2, 1003002):
    if nums[i]:
        plist.append(i)
        for j in range(2*i, 1003002, i):
            nums[j] = False
N = int(input())
result = 0
for i in range(N, 1003003):
    if i == 1:
        continue
    if str(i) == str(i)[::-1]:
        if i in plist:
            result = i
            break
print(result)
