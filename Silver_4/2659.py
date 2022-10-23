def card(i):
    num = i
    for _ in range(3):
        i = (i % 1000)*10+i//1000
        if num > i:
            num = i
    return num


num = int(''.join(input().split()))
result = card(num)
first = 1111
count = 0
while first <= result:
    if card(first) == first:
        count += 1
    first += 1
print(count)
