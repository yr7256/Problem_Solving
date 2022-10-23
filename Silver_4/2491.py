N = int(input())
nums = list(map(int, input().split()))
incr = [1]*N
decr = [1]*N
for i in range(N-1):
    if nums[i] >= nums[i+1]:
        decr[i+1] = max(decr[i]+1, decr[i+1])
    if nums[i] <= nums[i+1]:
        incr[i+1] = max(incr[i]+1, incr[i+1])
print(max(max(incr), max(decr)))
