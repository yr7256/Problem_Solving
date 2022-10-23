N = int(input())
cute = 0
for i in range(N):
    a = int(input())
    if a == 1:
        cute += 1
    else:
        cute -= 1
if cute < 0:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')
