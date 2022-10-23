def ThueMorse(n):
    if n == 0:
        return 0
    else:
        if n % 2:
            return 1-ThueMorse(n//2)
        else:
            return ThueMorse(n//2)


k = int(input())
print(ThueMorse(k-1))
