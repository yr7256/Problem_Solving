import sys


def find_root(x):
    if x != arr[x]:
        arr[x] = find_root(arr[x])
    return arr[x]


sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [i for i in range(n+1)]
for _ in range(m):
    x, a, b = map(int, input().split())
    if x == 0:
        a, b = find_root(a), find_root(b)
        s, e = min(a, b), max(a, b)
        arr[e] = s
    else:
        if find_root(a) == find_root(b):
            print('YES')
        else:
            print('NO')
