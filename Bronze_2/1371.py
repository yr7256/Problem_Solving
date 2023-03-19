import sys
S = sys.stdin.read()
lst = [0]*26
for i in S:
    if i.isalpha():
        lst[ord(i)-97] += 1
ans = ''
for j in range(26):
    if lst[j] == max(lst):
        print(chr(97+j))
print(ans)
