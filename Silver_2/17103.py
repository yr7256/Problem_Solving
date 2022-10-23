nums = [False, False]+[True]*(999999)
for i in range(2, 1000001):
    if nums[i]:
        for j in range(2*i, 1000001, i):
            nums[j] = False
T = int(input())
for i in range(T):
    N = int(input())
    count = 0
    for i in range(N//2+1):
        if nums[i] and nums[N-i]:
            count += 1
    print(count)
