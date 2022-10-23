sum = 0
for _ in range(5):
    N = int(input())
    if N < 40:
        sum += 40
    else:
        sum += N
print(sum//5)
