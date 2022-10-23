minN, maxN = map(int, input().split())
size = maxN-minN+1
squarenono = [False]*(size)
i = 2
while i**2 <= maxN:
    s = minN//(i**2)
    if minN % (i**2) != 0:
        s += 1
    while s*(i**2) <= maxN:
        if not squarenono[s*(i**2)-minN]:
            squarenono[s*(i**2)-minN] = True
            # size -= 1
        s += 1
    i += 1
count = 0
for i in squarenono:
    if not i:
        count += 1
print(count)
