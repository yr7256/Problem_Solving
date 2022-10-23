import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
result = abs(N - 100)
if M != 0:
    B = set(map(str, input().split()))
else:
    B = set()
for i in range(999901):
    impossible = False
    for j in str(i):
        if j in B:
            impossible = True
            break
    if impossible:
        continue
    else:
        result = min(result, len(str(i))+abs(i-N))
print(result)
