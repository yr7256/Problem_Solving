N = int(input())
n_list = []
for i in range(N):
    num = int(input())
    n_list.append(num)
n_list = sorted(n_list)
for i in n_list:
    print(i)
