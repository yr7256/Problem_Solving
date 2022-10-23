N = int(input())
books = {}
for i in range(N):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1
best = max(books.values())
bestseller = []
for name, num in books.items():
    if num == best:
        bestseller.append(name)
bestseller.sort()
print(bestseller[0])
