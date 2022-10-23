import sys
input = sys.stdin.readline
N, r, c = map(int, input().split())
count = 0
while N > 0:
    square = (2**N)//2
    if N > 1:
        if square > r and square <= c:
            count += square**2
            c -= square
        elif square <= r and square > c:
            count += (square**2)*2
            r -= square
        elif square <= r and square <= c:
            count += (square**2)*3
            r -= square
            c -= square
    elif N == 1:
        if r == 0 and c == 1:
            count += 1
        elif r == 1 and c == 0:
            count += 2
        elif r == 1 and c == 1:
            count += 3
    N -= 1
print(count)
