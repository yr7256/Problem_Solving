N = int(input())
arr = list(map(int, input().split()))
stack = [[] for _ in range(4)]
ans = 'YES'
for i in range(N):
    flag = True
    for j in range(4):
        if not stack[j] or stack[j][-1] < arr[i]:
            stack[j].append(arr[i])
            flag = False
            break
    if flag:
        ans = 'NO'
        break
print(ans)
