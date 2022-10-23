S = input()
s = input()
count = 0
n = 0
while n <= len(S)-len(s):
    if S[n:n+len(s)] == s:
        count += 1
        n += len(s)
    else:
        n += 1
print(count)
