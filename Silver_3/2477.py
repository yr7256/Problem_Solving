K = int(input())
lst = []
for i in range(6):
    d, l = map(int, input().split())
    lst.append(l)
lst = lst*2
max_f = 0
min_f = 0
max_i = 0
for i in range(6):
    temp = lst[i]*lst[i+1]
    if max_f < temp:
        max_f = temp
        max_i = i
min_f = lst[max_i+3]*lst[max_i+4]
print(K*(max_f-min_f))
