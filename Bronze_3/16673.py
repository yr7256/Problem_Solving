C, K, P = map(int, input().split())
print(P*C*(C+1)*(2*C+1)//6+(K*C*(C+1))//2)
