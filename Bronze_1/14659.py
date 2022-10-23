N = int(input())
lst = list(map(int, input().split()))
ans = []
h = 0
count = 0
for i in lst:
    if i > h:
        h = i
        count = 0
    else:
        count += 1
    ans.append(count)
print(max(ans))
