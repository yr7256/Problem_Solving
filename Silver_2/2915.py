B = input()
if B[:2] == 'LX' and B[:3] != 'LXX':
    B = B.replace('LX', 'XL')
if B[-2:] == 'XI':
    B = B.replace('XI', 'IX')
if B[:2] == 'LX' and B[:3] != 'LXX': # 과정 추가함
    B = B.replace('LX', 'XL')
'''
위 코드 안넣었을때 반례
LXXI(71) -> LXIX(69)로만 바뀌는데 LXIX(69) -> LXIX(49) 로도 바뀌어야 한다.
'''
if B[-2:] == 'VI':
    B = B.replace('VI', 'IV')
print(B)
