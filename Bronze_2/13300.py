N, K = map(int, input().split())
people = [[0, 0] for _ in range(7)]
ans = 0
for i in range(N):
    S, Y = map(int, input().split())
    people[Y][S] += 1
for grade in people:
    for num in grade:
        ans += num//K
        if num % K:
            ans += 1
print(ans)
