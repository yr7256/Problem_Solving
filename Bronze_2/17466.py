N, P = map(int, input().split())
ans = 1
for i in range(N, 1, -1):
    ans = (ans*i)%P
print(ans)
