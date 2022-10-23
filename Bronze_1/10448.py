tri = [i*(i+1)//2 for i in range(1, 46)]
eureka = [0]*1001
for i in tri:
    for j in tri:
        for k in tri:
            if i+j+k <= 1000:
                eureka[i+j+k] = 1
T = int(input())
for i in range(T):
    K = int(input())
    print(eureka[K])
