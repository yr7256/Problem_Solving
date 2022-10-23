c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
A = input()
for i in c:
    if i in A:
        A = A.replace(i, '*')
print(len(A))
