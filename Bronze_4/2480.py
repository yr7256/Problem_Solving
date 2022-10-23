dice = list(map(int, input().split()))
dice.sort()
dice_set = set(dice)
if len(dice_set) == 1:
    print(1000*dice[0]+10000)
elif len(dice_set) == 2:
    print(100*dice[1]+1000)
else:
    print(dice[-1]*100)
