S = list(input())
lst = ''
for i in S:
    n = ord(i)-3
    if n < ord('A'):
        n += 26
    lst += chr(n)
print(lst)
