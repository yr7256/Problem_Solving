N = int(input())
x = 1
count = 0
for i in map(int, input().split()):
    if x == i:
        count += 1
    x += 1
print(N-count)
