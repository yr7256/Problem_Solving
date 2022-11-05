import sys
input = sys.stdin.readline
N, H0 = map(int, input().split())
ans = 0
temp = 0  # 현재 체력
for i in range(N):
    t, a, h = map(int, input().split())  # 분류, 공격력, 체력
    if t == 1:
        q, r = h // H0, h % H0
        if r:
            temp -= a*q
        else:
            temp -= a*(q-1)
    else:
        H0 += a
        temp += h
    if temp > 0:
        temp = 0
    ans = max(ans, abs(temp))
print(ans+1)

