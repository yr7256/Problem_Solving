import sys
input = sys.stdin.readline
N = int(input())
profile = [list(input().split()) for i in range(N)]
profile.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in profile:
    print(i[0])
