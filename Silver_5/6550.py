while True:
    try:
        s, t = input().split()
        idx = 0
        flag = False
        for i in t:
            if i == s[idx]:
                idx += 1
                if idx == len(s):
                    flag = True
                    break
        if flag:
            print('Yes')
        else:
            print('No')
    except:
        break
