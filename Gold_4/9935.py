string = input()
bomb = input()
arr = []
for i in string:
    arr.append(i)
    if bomb[-1] == i and ''.join(arr[-len(bomb):]) == bomb:
        del arr[-len(bomb):]
if arr:
    print(''.join(arr))
else:
    print('FRULA')
