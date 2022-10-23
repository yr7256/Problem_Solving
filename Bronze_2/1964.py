N = int(input())
ans = 5
temp = 7
for i in range(1, N):
    ans += temp
    temp += 3
print(ans % 45678)
