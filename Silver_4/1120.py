A, B = input().split()
B = list(B)
cnt_list = []
while len(A) <= len(B):
    count = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            count += 1
    cnt_list.append(count)
    del B[0]
print(min(cnt_list))
