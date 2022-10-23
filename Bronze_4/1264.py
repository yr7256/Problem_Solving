vowel = ['a', 'e', 'i', 'o', 'u']
while True:
    s = input().lower()
    count = 0
    if s == '#':
        break
    for i in s:
        if i in vowel:
            count += 1
    print(count)
