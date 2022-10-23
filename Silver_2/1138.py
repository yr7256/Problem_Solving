N = int(input())
P = list(map(int, input().split()))
B = [0] * N
for i in range(N):
    count = 0
    for j in range(N):
        if count == P[i] and B[j] == 0:
            B[j] = i+1
            break
        elif B[j] == 0:
            count += 1
print(*B)
