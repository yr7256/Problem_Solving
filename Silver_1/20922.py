from collections import defaultdict
N, K = map(int, input().split())
lst = list(map(int, input().split()))
left, right = 0, 0
temp = 0
dic = defaultdict(int)
while right < N:
    if dic[lst[right]] < K:
        dic[lst[right]] += 1
        right += 1
    else:
        dic[lst[left]] -= 1
        left += 1
    temp = max(temp, right-left)
print(temp)
