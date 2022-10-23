def numsum(x):
    result = 0
    for i in x:
        if i.isdigit():
            result += int(i)
    return result


N = int(input())
serial = []
for i in range(N):
    serial.append(input())
serial.sort(key=lambda x: (len(x), numsum(x), x))
for i in serial:
    print(i)
