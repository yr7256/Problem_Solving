T = int(input())
for _ in range(T):
    n = int(input())
    room = [0]*n
    k = 1
    while k <= n:
        for i in range(k-1, n, k):
            if room[i] == 0:
                room[i] = 1
            else:
                room[i] = 0
        k += 1
    print(room.count(1))

# T = int(input())
# for _ in range(T):
#     n = int(input())
#     print(int(n**0.5))
