A, B = map(int, input().split())
count = 1
while True:
    if B == A:
        break
    elif B % 2 != 0 and B % 10 != 1 or B < A:
        count = -1
        break
    else:
        if B % 10 == 1:
            B //= 10
            count += 1
        else:
            B //= 2
            count += 1
print(count)
