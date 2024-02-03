N, X = map(int, input().split())
arr = list(map(int, input().split()))
temp = sum(arr[:X])
max_temp = temp
ans = 1
for i in range(X, N):
    temp = temp + arr[i] - arr[i-X]
    if max_temp == temp:
        ans += 1
    if max_temp < temp:
        max_temp = temp
        ans = 1
if max_temp:
    print(max_temp)
    print(ans)
else:
    print('SAD')