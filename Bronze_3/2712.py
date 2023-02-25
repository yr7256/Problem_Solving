n_dic = {'kg': 2.2046, 'l': 0.2642, 'g': 3.7854, 'lb': 0.4536}
s_dic = {'kg': 'lb', 'l': 'g', 'lb': 'kg', 'g': 'l'}
T = int(input())
for i in range(T):
    n, s = input().split()
    print(f'{(float(n)*n_dic[s]):.4f} {s_dic[s]}')
