first = [500, 300, 200, 50, 30, 10]
second = [512, 256, 128, 64, 32]
price1, price2 = [0], [0]
for i in range(6):
    price1 += [first[i] for _ in range(i+1)]
for i in range(5):
    price2 += [second[i] for _ in range(2**i)]
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    if a > 21:
        a = 0
    if b > 31:
        b = 0
    print((price1[a]+price2[b])*10000)
