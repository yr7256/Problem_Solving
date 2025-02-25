S = input()
target = 65
temp = 0
ans = 0
for i in S:
    if ord(i) == target or ord(i) == target+1:
        target = ord(i)
        if ord(i) == 90:
            ans += temp
    else:
        target = 65
        temp = 0
    if ord(i) == 65:
        temp += 1
print(ans)
