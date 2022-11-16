L = int(input())
A = input()
sum = 0
for i in range(L):
    sum += (ord(A[i])-96)*(31**i)
print(sum % 1234567891)
