N, S = map(int, input().split())
nums = list(map(int, input().split()))
left, right = 0, 0
psum = 0
sum_length = 100001
while True:
    if psum >= S:
        sum_length = min(sum_length, right-left)
        psum -= nums[left]
        left += 1
    else:
        psum += nums[right]
        if right == N:
            break
        right += 1
if sum_length == 100001:
    print(0)
else:
    print(sum_length)
