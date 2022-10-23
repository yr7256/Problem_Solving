N = int(input())
pat = list(map(str, input().split('*')))
for i in range(N):
    file = input()
    if len(file) >= len(pat[0])+len(pat[1]):
        if pat[0] == file[:len(pat[0])] and pat[1] == file[len(file)-len(pat[1]):]:
            print('DA')
        else:
            print('NE')
    else:
        print('NE')
