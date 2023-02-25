T = int(input())
for i in range(T):
    A, B = input().split()
    if sorted(list(A)) == sorted(list(B)):
        print(f'{A} & {B} are anagrams.')
    else:
        print(f'{A} & {B} are NOT anagrams.')
