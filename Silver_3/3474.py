import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    N = int(input())
    count = 0
    i = 5
    while i <= N:
        count += N//i
        i *= 5
    print(count)
