def check(string, start, end):
    while start < end:
        if string[start] != string[end]:
            return 0
        start += 1
        end -= 1
    return 1


S = input()
l = len(S)
if not check(S, 0, l-1):
    print(l)
elif not check(S, 0, l-2):
    print(l-1)
else:
    print(-1)