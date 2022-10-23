N = int(input())
scores = []
for n in range(N):
    cards = list(map(int, input().split()))
    max_num = 0
    for i in range(5):
        for j in range(i+1, 5):
            for k in range(j+1, 5):
                temp = (cards[i]+cards[j]+cards[k]) % 10
                max_num = max(max_num, temp)
    scores.append([n+1, max_num])
scores.sort(key=lambda x: (-x[1], -x[0]))
print(scores[0][0])
