import sys

input = sys.stdin.readline
piano = ['A', 'X', 'B', 'C', 'X', 'D', 'X', 'E', 'F', 'X', 'G', 'X']
N = int(input())
ans = []
nums = [int(input()) for _ in range(N)]
for i in range(12):
    target = i
    for n in nums:
        target = (target + n) % 12
        if piano[target] == 'X':
            break
    else:
        ans.append([piano[i], piano[target]])
for a in ans:
    print(*a)