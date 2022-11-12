T = int(input())
for _ in range(T):
    k = int(input())
    lst = [input() for _ in range(k)]
    for i in range(len(lst)):
        flag = True
        for j in range(len(lst)):
            if i != j:
                s = lst[i]+lst[j]
                if s == s[::-1]:
                    print(s)
                    flag = False
                    break
        if not flag:
            break
    else:
        print(0)