N = int(input())
P = int(input())
ans = 50000
if N >= 5:
    ans = min(ans, P-500)
if N >= 10:
    ans = min(ans, P*0.9)
if N >= 15:
    ans = min(ans, P-2000)
if N >= 20:
    ans = min(ans, P*0.75)
print(int(ans) if ans > 0 else 0)
