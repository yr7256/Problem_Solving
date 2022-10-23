import sys
input = sys.stdin.readline
N = int(input())
com = 0
for i in range(N):
    m = int(input())
    com += m
print(com-(N-1))
