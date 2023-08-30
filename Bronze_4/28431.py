lst = []
for _ in range(5):
    a = int(input())
    if a in lst:
        lst.remove(a)
    else:
        lst.append(a)
print(lst[0])
