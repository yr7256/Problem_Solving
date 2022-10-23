A = input().split('-')
N = []
for i in A:
    count = 0
    s = i.split('+')
    for j in s:
        count += int(j)
    N.append(count)
n = N[0]
for k in range(1, len(N)):
    n -= N[k]
print(n)
