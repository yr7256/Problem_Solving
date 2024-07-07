from math import gcd
n = int(input())
nums = list(map(int, input().split()))
arr = []
for i in range(n-1):
    for j in range(i+1, n):
        temp = nums[j]-nums[i]
        if temp:
            arr.append(temp)
ans = arr[0]
for i in range(1, len(arr)):
    ans = gcd(ans, arr[i])
print(ans)
