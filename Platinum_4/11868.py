N = int(input())
lst = list(map(int,input().split()))
ans = 0
for i in range(N):
    ans ^= lst[i]
if ans:
    print('koosaga')
else:
    print('cubelover')
