N = int(input())
x, y = [], []
answer = 0
for i in range(N):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
x = x+[x[0]]
y = y+[y[0]]
for i in range(N):
    answer += (x[i]*y[i+1])-(x[i+1]*y[i])
print(round(abs(answer)/2, 1))
