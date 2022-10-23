import sys
input = sys.stdin.readline
N = int(input())
A = []
count = 0
end = 0
for _ in range(N):
    a, b = map(int, input().split())
    A.append([a, b])
A.sort(key=lambda x: (x[1], x[0]))
for i, j in A:
    if i >= end:
        count += 1
        end = j
print(count)
