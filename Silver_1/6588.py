import sys
input = sys.stdin.readline


def P_n(i):
    if i == 1:
        return False
    else:
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                return False
        return True


prime = [True for i in range(1000001)]
for i in range(2, 1000001):
    if P_n(i) == False:
        prime[i] = False
while True:
    n = int(input())
    if n == 0:
        break
    for i in range(3, 1000000):
        if prime[i] and prime[n-i]:
            print(f"{n} = {i} + {n-i}")
            break
        i += 1
    else:
        print("Goldbach's conjecture is wrong.")
