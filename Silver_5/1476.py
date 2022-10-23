E1, S1, M1, count = 1, 1, 1, 1
E, S, M = map(int, input().split())
while(True):
    if E == E1 and S == S1 and M == M1:
        break
    E1 += 1
    S1 += 1
    M1 += 1
    count += 1
    if E1 >= 16:
        E1 -= 15
    if S1 >= 29:
        S1 -= 28
    if M1 >= 20:
        M1 -= 19
print(count)
