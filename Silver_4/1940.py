N = int(input())
M = int(input())
lst = list(map(int, input().split()))
lst.sort()
count = 0
left = 0
right = N-1
while left < right:
    if lst[left]+lst[right] == M:
        count += 1
        left += 1
        right -= 1
    elif lst[left]+lst[right] < M:
        left += 1
    elif lst[left]+lst[right] > M:
        right -= 1
print(count)
