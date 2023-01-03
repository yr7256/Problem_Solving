N = int(input())
lst = list(map(int, input().split()))
me, opp = sum(lst[0::2]), sum(lst[0::2])
ans = me
for i in range(N-1, 0, -2):
    me += lst[i]-lst[i-1]
    ans = max(ans, me)
for j in range(N-2, 0, -2):
    opp += lst[j-1]-lst[j]
    ans = max(ans, opp)
print(ans)
