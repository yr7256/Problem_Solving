N = int(input())
arr = list(map(int, input().split()))
ans = [arr[0]]
for i in range(1, N):
    ans.append(arr[i]*(i+1)-sum(ans))
print(*ans)
