t = int(input())
for i in range(t):
    n = int(input())
    for i in range(2, n+1):
        count = 0
        if n % i == 0:
            while n % i == 0:
                n //= i
                count += 1
            print(i, count)
        elif n == 1:
            break
