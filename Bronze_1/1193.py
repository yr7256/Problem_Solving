N = int(input())
line = 1
while N > line:
    N -= line
    line += 1
if line % 2 == 1:
    A = line+1-N
    B = N
else:
    A = N
    B = line+1-N
print(A, "/", B, sep='')
