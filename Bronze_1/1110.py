A = input()
if len(A) < 2:
    A = "0"+A
A0 = A
count = 0
while True:
    A1 = str((int(A[0])+int(A[1])))
    if len(A1) < 2:
        A1 = "0"+A1
    A = A[1]+A1[1]
    count += 1
    if A0 == A:
        break
print(count)
