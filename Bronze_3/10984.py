T = int(input())
for _ in range(T):
    N = int(input())
    total = 0
    gpa = 0
    for _ in range(N):
        C, G = map(float, input().split())
        total += C
        gpa += C*G
    gpa /= total
    print(int(total), round(gpa, 1))