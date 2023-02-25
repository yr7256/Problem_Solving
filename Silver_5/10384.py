from collections import defaultdict

T = int(input())
for t in range(T):
    dic = defaultdict(int)
    for i in input().lower():
        if i.isalpha():
            dic[i] += 1
    if len(dic) == 26:
        if min(dic.values()) == 1:
            print(f'Case {t+1}: Pangram!')
        elif min(dic.values()) == 2:
            print(f'Case {t+1}: Double pangram!!')
        else:
            print(f'Case {t+1}: Triple pangram!!!')
    else:
        print(f'Case {t+1}: Not a pangram')
