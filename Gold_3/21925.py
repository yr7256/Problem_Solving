N = int(input())
arr = [0]+list(map(int, input().split()))
is_palindrome = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    s, e = i, i+1
    while s >= 1 and e <= N and arr[s] == arr[e]:
        is_palindrome[s][e] = 1
        s -= 1
        e += 1
dp = [-1]*(N+1)
dp[0] = 0
for i in range(1, N+1):
    for j in range(i-1, 0, -2):
        if is_palindrome[j][i] and dp[j-1] != -1:
            dp[i] = max(dp[i], dp[j-1]+1)
print(dp[N])
