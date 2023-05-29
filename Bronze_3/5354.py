t = int(input())
for _ in range(t):
    n = int(input())
    if n < 3:
        for i in range(n):
            print('#'*n)
    else:
        print('#'*n)
        for i in range(n-2):
            print('#'+'J'*(n-2)+'#')
        print('#'*n)
    print()
