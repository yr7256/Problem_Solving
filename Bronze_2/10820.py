while True:
    try:
        S = input()
    except:
        break
    l, u, n, b = 0, 0, 0, 0
    for i in S:
        if i.islower():
            l += 1
        elif i.isupper():
            u += 1
        elif i.isdigit():
            n += 1
        elif i.isspace():
            b += 1
    print(l, u, n, b)
