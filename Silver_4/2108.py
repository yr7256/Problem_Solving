import sys
import collections
N = int(sys.stdin.readline())
A = []
for _ in range(N):
    a = int(sys.stdin.readline())
    A.append(a)
A.sort()
A_1 = collections.Counter(A).most_common()
print(round(sum(A)/N))
print(A[N//2])
if len(A) > 1:
    if A_1[0][1] == A_1[1][1]:
        print(A_1[1][0])
    else:
        print(A_1[0][0])
else:
    print(A_1[0][0])
print(A[-1]-A[0])
