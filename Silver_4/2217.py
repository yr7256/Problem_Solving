import sys
input = sys.stdin.readline
N = int(input())
rope = []
for _ in range(N):
    A = int(input())
    rope.append(A)
rope.sort()
result = 0
for i in range(len(rope)):
    if result < N*rope[i]:
        result = N*rope[i]
        N -= 1
    else:
        N -= 1
print(result)
