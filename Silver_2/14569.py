N = int(input())
cla_info = []
for i in range(N):
    cla_info.append(set(list(map(int, input().split()))[1:]))
M = int(input())
stu_info = []
for i in range(M):
    stu_info.append(set(list(map(int, input().split()))[1:]))
for stu in stu_info:
    count = 0
    for cla in cla_info:
        if cla.intersection(stu) == cla:
            count += 1
    print(count)
