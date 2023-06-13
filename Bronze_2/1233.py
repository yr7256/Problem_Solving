s1, s2, s3 = list(map(int, input().split()))
a = [0]*81
for i in range(1, s1+1):
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            a[i+j+k] += 1
for i in range(1, 81):
    if a[i] == max(a):
        print(i)
        break
