while True:
    try:
        n = int(input())
    except:
        break
    num = 0
    i = 1
    while True:
        num = num*10+1
        if num % n == 0:
            print(i)
            break
        i += 1
