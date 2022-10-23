import sys
input = sys.stdin.readline
X, Y = map(int, input().split())
Z = Y*100//X
floor, ceil = 0, 1000000000
if Z >= 99:
    print(-1)
else:
    while floor <= ceil:
        round = (floor+ceil)//2
        x1, y1 = X+round, Y+round
        if y1*100//x1 > Z:
            ceil = round-1
        else:
            floor = round+1
    print(floor)
