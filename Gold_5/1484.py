G = int(input())
left, right = 1, 1
ans = []
while left+right <= G:
    weight = (right+left)*(right-left)
    if weight == G:
        ans.append(right)
        right += 1
    elif weight < G:
        right += 1
        continue
    else:
        left += 1
if ans:
    for i in ans:
        print(i)
else:
    print(-1)
