import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    zero = 1
    one = 0
    temp = 0
    for _ in range(N):
        temp = one
        one = one+zero
        zero = temp
    print(zero, one)
