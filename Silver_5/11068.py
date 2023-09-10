T = int(input())
for _ in range(T):
    N = int(input())
    for i in range(2, 65):
        num = []
        temp = N
        while temp:
            num.append(temp % i)
            temp //= i
        if num == num[::-1]:
            print(1)
            break
    else:
        print(0)