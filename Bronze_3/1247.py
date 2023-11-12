import sys
input = sys.stdin.readline
for i in range(3):
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    if sum(arr) > 0:
        print('+')
    elif sum(arr) < 0:
        print('-')
    else:
        print(0)
