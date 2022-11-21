import sys
input = sys.stdin.readline
N = int(input())
for i in range(N):
    if int(input().strip()[-1]) % 2:
        print('odd')
    else:
        print('even')
