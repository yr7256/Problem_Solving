import sys
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]
ans = -1
arr.sort()
for i in range(N-1, 1, -1):
    if arr[i] < arr[i-1] + arr[i-2]:
        ans = arr[i] + arr[i-1] + arr[i-2]
        break
print(ans)
