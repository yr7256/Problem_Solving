import sys
input = sys.stdin.readline
N = int(input())
field = [list(map(int, input().split())) for i in range(N)]
maxL, maxC, maxR = field[0][0], field[0][1], field[0][2]
minL, minC, minR = field[0][0], field[0][1], field[0][2]
for i in range(1, N):
    maxL, maxC, maxR = field[i][0]+max(maxL, maxC), field[i][1] + \
        max(maxL, maxC, maxR), field[i][2]+max(maxC, maxR)
    minL, minC, minR = field[i][0]+min(minL, minC), field[i][1] + \
        min(minL, minC, minR), field[i][2]+min(minC, minR)
print(max(maxL, maxC, maxR), min(minL, minC, minR))
