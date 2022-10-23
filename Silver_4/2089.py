N = int(input())
M = N
result = ''
while N:
    if N % -2 != 0:
        result = '1' + result
        N = N//-2 + 1
    else:
        result = '0' + result
        N = N//-2
if M == 0:
    print(0)
else:
    print(result)
