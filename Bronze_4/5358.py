while True:
    try:
        s = list(input())
        for i in range(len(s)):
            if s[i] == 'e':
                s[i] = 'i'
            elif s[i] == 'i':
                s[i] = 'e'
            elif s[i] == 'I':
                s[i] = 'E'
            elif s[i] == 'E':
                s[i] = 'I'
        print(''.join(s))
    except:
        exit(0)
