N = int(input())
max_lst = []
for i in range(1, N+1):
    lst = [N, i]
    temp = 0
    while True:
        last = lst[temp]-lst[temp+1]
        if last < 0:
            break
        lst.append(last)
        temp += 1
    if len(max_lst) < len(lst):
        max_lst = lst
print(len(max_lst))
print(*max_lst)
