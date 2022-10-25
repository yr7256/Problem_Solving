import sys
from math import log2


def onecnt(n):
    if n <= 0:
        return 0
    square = 2**int(log2(n))
    diff = n - square
    if diff == 0:
        return int(log2(n))*n//2+1
    return onecnt(square)+onecnt(diff)+diff


input = sys.stdin.readline
A, B = map(int, input().split())
print(onecnt(B)-onecnt(A-1))
