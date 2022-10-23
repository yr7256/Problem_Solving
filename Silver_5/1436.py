N = int(input())
count = 0
start = 666
while True:
    if '666' in str(start):
        count += 1
    if count == N:
        print(start)
        break
    start += 1
