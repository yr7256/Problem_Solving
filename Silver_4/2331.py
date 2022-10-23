def p(x):
    x = int(x)**P
    return x


A, P = map(int, input().split())
A_list = [A]
i = 0
while True:
    num = sum(map(p, str(A_list[i])))
    i += 1
    if num in A_list:
        break
    A_list.append(num)
print(A_list.index(num))
