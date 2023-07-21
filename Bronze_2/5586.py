S = input()
a, b = 0, 0
for i in range(len(S)-2):
    if S[i:i+3] == 'JOI':
        a += 1
    if S[i:i+3] == 'IOI':
        b += 1
print(a)
print(b)
