while True:
    try:
        N = int(input())
        s = '-'
        for i in range(1, N+1):
            s = s+' '*len(s)+s
        print(s)
    except:
        break
