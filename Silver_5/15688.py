import sys
input = sys.stdin.readline
N = int(input())
lst = [int(input()) for i in range(N)]
lst.sort()
for i in lst:
    print(i)
