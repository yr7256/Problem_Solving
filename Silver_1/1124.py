A, B = map(int, input().split())
nums = [i for i in range(100001)]
for i in range(2, int(100000**0.5)+1):
    if nums[i] == i:
        for j in range(i*i, 100001, i):
            if nums[j] == j:
                nums[j] = i
nums[0], nums[1] = 0, 0
ans = 0
for i in range(A, B+1):
    cnt = 0
    while nums[i] > 1:
        cnt += 1
        i //= nums[i]
    if nums[cnt] == cnt:
        ans += 1
print(ans)
