N = int(input())
s = list(map(int, input().split()))
M = int(input())
left, right = 0, max(s)
while left <= right:
    mid = (left+right)//2
    budget = 0
    for i in s:
        if i <= mid:
            budget += i
        else:
            budget += mid
    if budget <= M:
        left = mid+1
    else:
        right = mid-1
print(right)
