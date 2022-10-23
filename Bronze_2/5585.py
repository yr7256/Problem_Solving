coin = [500, 100, 50, 10, 5, 1]
N = int(input())
A = 1000-N
count = 0
for i in coin:
    count += A//i
    A %= i
print(count)
