n = int(input())
lst = list(map(int, input().split()))
temp = 0
ans = 0
for i in range(n-1):
    temp += lst[i]
    ans += lst[i+1]*temp
print(ans)
