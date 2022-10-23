lst = []
x, y = 0, 0
for i in range(9):
    lst.append(int(input()))
for i in range(8):
    for j in range(i+1, 9):
        if sum(lst)-lst[i]-lst[j] == 100:
            x, y = i, j
lst.pop(x)
lst.pop(y-1)
for i in lst:
    print(i)
