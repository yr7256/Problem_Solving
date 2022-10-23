N, K, L = map(int, input().split())
count = 0
while K != L:
    K -= K//2
    L -= L//2
    count += 1
print(count)
