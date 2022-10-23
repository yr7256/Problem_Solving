S = int(input())
switch = [0]+list(map(int, input().split()))
P = int(input())


def change(i):
    if switch[i] == 0:
        switch[i] = 1
    else:
        switch[i] = 0


for i in range(P):
    gen, num = map(int, input().split())
    if gen == 1:
        for i in range(num, S+1, num):
            change(i)
    else:
        if num+1 > S or num-1 < 1:
            change(num)
        else:
            if switch[num-1] == switch[num+1]:
                left = num-1
                right = num+1
                while True:
                    if left-1 < 1 or right+1 > S:
                        break
                    if switch[left-1] != switch[right+1]:
                        break
                    else:
                        left -= 1
                        right += 1
                for i in range(left, right+1):
                    change(i)
            else:
                change(num)
for i in range(1, S+1, 20):
    print(*switch[i:i+20])
print(switch)
