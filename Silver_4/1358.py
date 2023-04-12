from math import dist

W, H, X, Y, P = map(int, input().split())
x1, y1 = X, Y+H//2
x2, y2 = X+W, Y+H//2
ans = 0
for i in range(P):
    x, y = map(int, input().split())
    if (X <= x <= X+W and Y <= y <= Y+H) or min(dist((x1, y1), (x, y)), dist((x2, y2), (x, y))) <= H//2:
        ans += 1
print(ans)
