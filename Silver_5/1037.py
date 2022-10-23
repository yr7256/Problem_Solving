import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
print(min(A)*max(A))
