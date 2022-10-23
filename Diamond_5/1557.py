def squarefree(num):
    ans = 0
    for i in range(1, int(num**0.5)+1):
        ans += mobius[i]*(num//i**2)
    return ans


mobius = [0] * 45001
K = int(input())
mobius[1] = 1
for i in range(1, 45001):
    if mobius[i]:
        for j in range(i * 2, 45001, i):
            mobius[j] -= mobius[i]
start, end = 0, 2000000000
while start <= end:
    mid = (start+end) // 2
    if squarefree(mid) < K:
        start = mid+1
    else:
        end = mid-1
print(start)
# print(squarefree(K))
