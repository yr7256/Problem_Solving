import sys
input = sys.stdin.readline

N = int(input())
scores = [float(input()) for _ in range(N)]
scores.sort()
for i in range(7):
    print(f"{scores[i]:.3f}")