v = ['a', 'e', 'i', 'o', 'u']
N = int(input())
cnt = 0
for i in input():
    if i in v:
        cnt += 1
print(cnt)
