import sys
input = sys.stdin.readline
N, M = map(int, input().split())
list_l = set()
list_s = set()
for i in range(N):
    a = input()
    list_l.add(a)
for j in range(M):
    b = input()
    list_s.add(b)
A = sorted(list(list_l & list_s))
print(len(A))
for k in A:
    print(k, end='')
