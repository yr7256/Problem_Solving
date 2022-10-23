A = list(input())
B = list(input())
LCS = [[0 for i in range(len(B)+1)] for i in range(len(A)+1)]
for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            LCS[i+1][j+1] = LCS[i][j]+1
        else:
            LCS[i+1][j+1] = max(LCS[i][j+1], LCS[i+1][j])
print(LCS[len(A)][len(B)])
