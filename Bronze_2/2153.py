nums = [False, True]+[True]*(1039)
for i in range(2, 1041):
    if nums[i]:
        for j in range(2*i, 1041, i):
            nums[j] = False
s = input()
n = 0
for i in s:
    if i.islower():
        n += ord(i)-96
    else:
        n += ord(i)-38
if nums[n]:
    print('It is a prime word.')
else:
    print('It is not a prime word.')
