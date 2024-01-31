import sys
input = sys.stdin.readline
N, M = map(int, input().split())
flag = True
for _ in range(M):
    k = int(input())
    arr = list(map(int, input().split()))
    if arr != sorted(arr, reverse=True):
        flag = False
if flag:
    print('Yes')
else:
    print('No')
