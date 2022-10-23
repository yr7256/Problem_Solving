dic = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
       '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
M, N = map(int, input().split())
lst = []
for i in range(M, N+1):
    n = ' '.join([dic[j] for j in str(i)])
    lst.append([i, n])
lst.sort(key=lambda x: x[1])
for i in range(len(lst)):
    if i % 10 == 0 and i != 0:
        print()
    print(lst[i][0], end=' ')
