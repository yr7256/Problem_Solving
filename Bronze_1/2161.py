N = int(input())
card = [i for i in range(1, N+1)]
discard = []
while len(card) != 1:
    discard.append(card.pop(0))
    card.append(card.pop(0))
print(*discard, *card)
