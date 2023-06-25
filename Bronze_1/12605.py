N = int(input())
for i in range(N):
    a = list(input().split())
    a = a[::-1]
    print(f'Case #{i+1}:', *a)
