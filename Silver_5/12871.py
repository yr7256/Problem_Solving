from math import lcm
s = input()
t = input()
a = lcm(len(s), len(t))
if s*(a//len(s)) == t*(a//len(t)):
    print(1)
else:
    print(0)
