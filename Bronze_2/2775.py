T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    room = [i for i in range(1, n+1)]
    for _ in range(k):
        for j in range(1, n):
            room[j] += room[j-1]
    print(room[n-1])
