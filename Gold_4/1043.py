N, M = map(int, input().split())
know = set(list(map(int, input().split()))[1:])
truth = [1]*M
party_list = []
for _ in range(M):
    people = list(map(int, input().split()))[1:]
    party_list.append(people)
for _ in range(M):
    for i, party in enumerate(party_list):
        if know.intersection(set(party)):
            truth[i] = 0
            know = know.union(set(party))
print(sum(truth))
