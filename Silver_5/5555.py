s = input()
N = int(input())
count = 0
for i in range(N):
    ring = input()*2
    if s in ring:
        count += 1
print(count)
