N = int(input())
nums = list(map(int, input().split()))
sum_num = sum(nums)
ans = 0
for i in nums:
    sum_num -= i
    ans += sum_num*i
print(ans)
