N = int(input())
s = list(map(int, input().split()))
nums = [i for i in range(1, N+1)]
result = []
n = 0
b = s.pop(n)
result.append(nums.pop(n))
while s:
    if b > 0:
        n = (n+b-1) % len(s)
    else:
        n = (n+b) % len(s)
    b = s.pop(n)
    result.append(nums.pop(n))
print(*result)
