import sys
input = sys.stdin.readline
N = int(input())
s = []
for i in range(N):
    s.append(int(input()))
s.sort(reverse=True)
for i in s:
    print(i)
