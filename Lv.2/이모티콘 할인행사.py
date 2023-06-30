from itertools import product


def solution(users, emoticons):
    answer = [0, 0]
    discounts = [10, 20, 30, 40]
    for discount in product(discounts, repeat=len(emoticons)):
        temp = [0, 0]
        for target, cost in users:
            profit = 0
            for d, emoticon in zip(discount, emoticons):
                if target <= d:
                    profit += emoticon*(100-d)//100
            if profit >= cost:
                temp[0] += 1
            else:
                temp[1] += profit
        answer = max(answer, temp)
    return answer