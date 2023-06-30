def solution(s):
    lst = [['0', 'zero'], ['1', 'one'], ['2', 'two'], ['3', 'three'], ['4', 'four'], [
        '5', 'five'], ['6', 'six'], ['7', 'seven'], ['8', 'eight'], ['9', 'nine']]
    for i in lst:
        s = s.replace(i[1], i[0])
    return int(s)
